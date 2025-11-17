from ibm_watsonx_orchestrate.agent_builder.tools import tool
from datetime import date

# --- Mock Database ---
# A dictionary to simulate a database table for benefit enrollments.
# Key: employee_id, Value: list of enrolled benefit dictionaries.
BENEFIT_ENROLLMENTS = {
    "EMP001": [
        {
            "plan_id": "HEALTH01",
            "plan_name": "Premium Health Plan",
            "coverage_level": "Family",
            "enrollment_date": "2023-01-15",
            "monthly_cost": 450.00
        }
    ],
    "EMP003": [
        {
            "plan_id": "HEALTH01",
            "plan_name": "Premium Health Plan",
            "coverage_level": "Family",
            "enrollment_date": "2023-01-15",
            "monthly_cost": 450.00
        },
        {
            "plan_id": "DENTAL01",
            "plan_name": "Basic Dental Plan",
            "coverage_level": "Self",
            "enrollment_date": "2023-02-01",
            "monthly_cost": 45.50
        }
    ]
}

# List of valid employee IDs and available benefit plans for validation.
VALID_EMPLOYEE_IDS = {'EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005'}
VALID_BENEFIT_PLANS = {
    "HEALTH01": {"name": "Premium Health Plan", "cost": {"Self": 250.00, "Family": 450.00}},
    "DENTAL01": {"name": "Basic Dental Plan", "cost": {"Self": 45.50, "Family": 95.00}},
    "VISION01": {"name": "Standard Vision Plan", "cost": {"Self": 15.00, "Family": 35.00}}
}
# --- End Mock Database ---


@tool
def enroll_benefit(employee_id: str, plan_id: str, coverage_level: str) -> dict:
    """
    Enrolls an employee into a specified benefit plan.

    This function simulates enrolling an employee into a benefit plan like health, dental, or vision.
    It validates the employee ID, plan ID, and coverage level before recording the enrollment.
    If the employee is already enrolled in the specified plan, it updates the existing enrollment.

    Args:
        employee_id (str): The ID of the employee to enroll (e.g., 'EMP001'). Case-insensitive.
        plan_id (str): The ID of the benefit plan to enroll in (e.g., 'HEALTH01', 'DENTAL01'). Case-insensitive.
        coverage_level (str): The desired coverage level ('Self' or 'Family'). Case-insensitive.

    Returns:
        dict: A dictionary containing the status and a confirmation or error message.
    """
    emp_id = employee_id.upper()
    p_id = plan_id.upper()
    cov_level = coverage_level.title()

    # --- Input Validation ---
    if emp_id not in VALID_EMPLOYEE_IDS:
        return {"status": "Error", "message": f"Invalid Employee ID: {employee_id}"}
    if p_id not in VALID_BENEFIT_PLANS:
        return {"status": "Error", "message": f"Invalid Plan ID: {plan_id}"}
    if cov_level not in ['Self', 'Family']:
        return {"status": "Error", "message": f"Invalid Coverage Level: {coverage_level}. Must be 'Self' or 'Family'."}

    # --- Enrollment Logic ---
    plan_details = VALID_BENEFIT_PLANS[p_id]
    enrollment_record = {
        "plan_id": p_id,
        "plan_name": plan_details["name"],
        "coverage_level": cov_level,
        "enrollment_date": str(date.today()),
        "monthly_cost": plan_details["cost"][cov_level]
    }

    # Get current enrollments for the employee, or initialize if none exist
    current_enrollments = BENEFIT_ENROLLMENTS.get(emp_id, [])

    # Check if already enrolled, if so, remove old record to update it
    current_enrollments = [item for item in current_enrollments if item['plan_id'] != p_id]
    
    # Add the new/updated enrollment
    current_enrollments.append(enrollment_record)
    BENEFIT_ENROLLMENTS[emp_id] = current_enrollments

    return {
        "status": "Success",
        "message": f"Employee {emp_id} successfully enrolled in {plan_details['name']} with {cov_level} coverage."
    }


@tool
def view_benefit_enrollment(employee_id: str) -> dict:
    """
    Retrieves the current benefit enrollment details for a specified employee.

    Args:
        employee_id (str): The ID of the employee whose enrollments you want to view. Case-insensitive.

    Returns:
        dict: A dictionary containing the employee's enrollment status and a list of their enrolled benefits.
              Returns an error message if the employee ID is invalid.
    """
    emp_id = employee_id.upper()

    if emp_id not in VALID_EMPLOYEE_IDS:
        return {"status": "Error", "message": f"Invalid Employee ID: {employee_id}"}

    enrollments = BENEFIT_ENROLLMENTS.get(emp_id, [])

    if not enrollments:
        return {
            "employee_id": emp_id,
            "status": "Not Enrolled",
            "enrollments": []
        }
    
    return {
        "employee_id": emp_id,
        "status": "Enrolled",
        "enrollments": enrollments
    }
