from ibm_watsonx_orchestrate.agent_builder.tools import tool

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