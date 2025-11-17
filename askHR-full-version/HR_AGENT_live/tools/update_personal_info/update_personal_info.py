import pandas as pd
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def update_personal_info(
    employee_id,
    first_name=None,
    last_name=None,
    phone_number=None,
    email=None,
    department=None,
    job_title=None,
    hire_date=None,
    employment_status=None,
    manager_id=None,
    office_location=None
) -> str:
    """
    Updates personal information for a specified employee in employee_personal_info.csv (case-insensitive).
    Only the fields provided (not None) will be updated.

    Summary of Updatable Fields:
        - first_name
        - last_name
        - phone_number
        - email
        - department
        - job_title
        - hire_date
        - employment_status
        - manager_id
        - office_location

    Args:
        employee_id (str): Employee ID to update (case-insensitive).
        first_name (str, optional): Employee's first name.
        last_name (str, optional): Employee's last name.
        phone_number (str, optional): Employee's phone number.
        email (str, optional): Employee's email address.
        department (str, optional): Employee's department.
        job_title (str, optional): Employee's job title.
        hire_date (str, optional): Employee's hire date.
        employment_status (str, optional): Employee's employment status.
        manager_id (str, optional): Employee's manager ID.
        office_location (str, optional): Employee's office location.

    Returns:
        str: Success or error message.
    """
    try:
        # Read the CSV file
        # df = pd.read_csv('employee_personal_info.csv')
        df = pd.DataFrame({
            'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005'],
            'first_name': ['John', 'Sarah', 'Michael', 'Lisa', 'Robert'],
            'last_name': ['Smith', 'Johnson', 'Chen', 'Park', 'Kim'],
            'phone_number': ['+1-555-0101', '+1-555-0102', '+1-555-0103', '+1-555-0104', '+1-555-0105'],
            'email': ['john.smith@techcorp.com', 'sarah.johnson@techcorp.com', 'michael.chen@techcorp.com', 'lisa.park@techcorp.com', 'robert.kim@techcorp.com'],
            'department': ['Engineering', 'Marketing', 'Finance', 'Human Resources', 'Operations'],
            'job_title': ['Senior Software Engineer', 'Marketing Manager', 'Financial Analyst', 'HR Specialist', 'Operations Coordinator'],
            'hire_date': ['2022-03-15', '2021-07-01', '2023-01-10', '2020-05-20', '2019-11-08'],
            'employment_status': ['Active', 'Active', 'Active', 'Active', 'Active'],
            'manager_id': ['MGR001', 'MGR002', 'MGR003', 'MGR004', 'MGR005'],
            'office_location': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Denver'],
            'workday_profile_url': ['https://workday.com/profile/EMP001', 'https://workday.com/profile/EMP002', 'https://workday.com/profile/EMP003', 'https://workday.com/profile/EMP004', 'https://workday.com/profile/EMP005']
        })

        # Case-insensitive match for employee_id
        emp_mask = df['employee_id'].str.lower() == employee_id.lower()

        if not emp_mask.any():
            print(f"Employee {employee_id} not found")
            return f"Employee {employee_id} not found"

        # Update specified fields
        updated_fields = []
        field_map = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email': email,
            'department': department,
            'job_title': job_title,
            'hire_date': hire_date,
            'employment_status': employment_status,
            'manager_id': manager_id,
            'office_location': office_location
        }
        for field, value in field_map.items():
            if value is not None:
                df.loc[emp_mask, field] = value
                updated_fields.append(f"{field}: {value}")

        if not updated_fields:
            print("No valid fields to update")
            return "No valid fields to update"

        # Save updated DataFrame
        # df.to_csv('employee_personal_info.csv', index=False)

        success_message = f"Successfully updated {employee_id}:"
        for field in updated_fields:
            print(f"  - {field}")

        return success_message

    except FileNotFoundError:
        print("employee_personal_info.csv file not found")
        return "employee_personal_info.csv file not found"
    except Exception as e:
        print(f"Error updating employee info: {e}")
        return "Error updating employee info"

# Example usage:
if __name__ == "__main__":
    # Update single field for EMP001
    print(update_personal_info("EMP001", email="john.doe@newcompany.com"))

    # Update multiple fields for EMP002
    print(update_personal_info(
        "EMP002",
        department="IT",
        job_title="Senior Developer",
        phone_number="555-1234"
    ))

    # Update employment status for EMP003
    print(update_personal_info("EMP003", employment_status="Active"))