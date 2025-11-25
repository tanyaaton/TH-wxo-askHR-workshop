from ibm_watsonx_orchestrate.agent_builder.tools import tool
import pandas as pd

@tool
def get_personal_employee_info(employee_id: str) -> dict:
    """
    Retrieves personal information for a specified employee (case-insensitive) from a CSV file (mocked as a DataFrame).

    Summary of Personal Info Data:
        - Returns a dictionary with keys: employee_id, first_name, last_name, phone_number, email, department, job_title, hire_date, employment_status, manager_id, office_location, workday_profile_url.
        - Only data for the specified employee is returned. If not found, returns an empty dictionary.
        - employee_id: Identifier for the employee.
        - first_name: Employee's first name.
        - last_name: Employee's last name.
        - phone_number: Employee's contact phone number.
        - email: Employee's email address.
        - department: Department where the employee works.
        - job_title: Employee's job title.
        - hire_date: Date when the employee was hired.
        - employment_status: Current status of employment (e.g., Active, On Leave).
        - manager_id: Identifier for the employee's manager.
        - office_location: Location of the employee's office.
        - workday_profile_url: URL to the employee's Workday profile.

    Args:
        employee_id (str): Employee ID to look up (case-insensitive).

    Returns:
        dict: Dictionary with personal info details for the employee, or empty dict if not found.
    """
    try:
        # Read the CSV file
        # df = pd.read_csv('employee_personal_info.csv')  # Replace with your actual CSV filename
        df = pd.DataFrame({
            'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005'],
            'first_name': ['John', 'Sarah', 'Michael', 'Lisa', 'Robert'],
            'last_name': ['Smith', 'Johnson', 'Chen', 'Park', 'Kim'],
            'phone_number': ['+1-555-0101', '+1-555-0102', '+1-555-0103', '+1-555-0104', '+1-555-0105'],
            'email': ['john.smith@techcorp.com', 'sarah.johnson@techcorp.com', 'michael.chen@techcorp.com', 'lisa.park@techcorp.com', 'robert.kim@techcorp.com'],
            'department': ['Sale', 'Sale', 'Sale', 'Sale', 'Sale'],
            'job_title': ['Manager', 'Marketing', 'Financial Analyst', 'HR Specialist', 'Operations Coordinator'],
            'hire_date': ['2022-03-15', '2021-07-01', '2023-01-10', '2020-05-20', '2019-11-08'],
            'employment_status': ['Active', 'Active', 'Active', 'Active', 'Active'],
            'manager_id': ['MGR001', 'MGR002', 'MGR003', 'MGR004', 'MGR005'],
            'office_location': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Denver'],
            'workday_profile_url': ['https://workday.com/profile/EMP001', 'https://workday.com/profile/EMP002', 'https://workday.com/profile/EMP003', 'https://workday.com/profile/EMP004', 'https://workday.com/profile/EMP005']
        })

        # Case-insensitive match for employee_id
        mask = df['employee_id'].str.lower() == employee_id.lower()
        filtered_df = df[mask]

        # Check if any rows match
        if filtered_df.empty:
            print(f"No employee with ID {employee_id} found")
            return {}

        # Convert the first matching row to dictionary
        result_dict = filtered_df.iloc[0].to_dict()

        return result_dict

    except FileNotFoundError:
        print("CSV file not found")
        return {}
    except KeyError as e:
        print(f"Column not found: {e}")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

@tool 
def get_payment_employee_info(employee_id: str) -> dict:
    """
    Reads a CSV file, filters for a specified employee ID (case-insensitive), and returns the row data as a dictionary.

    Args:
        employee_id (str): Employee ID to look up (case-insensitive).

    Returns:
        dict: Dictionary with column headers as keys and row values as values. Returns empty dict if not found.
    """
    try:
        # Read the CSV file
        # df = pd.read_csv('employee_payment_info.csv')  # Replace with your actual CSV filename
        df = pd.DataFrame({
            'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005'],
            'bank_name': ['Chase Bank', 'Bank of America', 'Wells Fargo', 'Citibank', 'US Bank'],
            'bank_account_number': ['****1234', '****5678', '****9012', '****3456', '****7890'],
            'routing_number': [21000021, 21000021, 21000021, 21000021, 21000021],
            'branch_code': ['NY001', 'LA002', 'CHI003', 'NY004', 'DEN005'],
            'account_type': ['Checking', 'Checking', 'Checking', 'Checking', 'Checking'],
            'payment_method': ['Direct Deposit', 'Direct Deposit', 'Direct Deposit', 'Direct Deposit', 'Direct Deposit'],
            'direct_deposit_active': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes'],
            'last_updated': ['2024-01-15', '2023-12-20', '2024-02-10', '2023-11-05', '2024-03-01']
        })

        # Case-insensitive match for employee_id
        mask = df['employee_id'].str.lower() == employee_id.lower()
        filtered_df = df[mask]

        # Check if any rows match
        if filtered_df.empty:
            print(f"No employee with ID {employee_id} found")
            return {}

        # Convert the first matching row to dictionary
        result_dict = filtered_df.iloc[0].to_dict()

        return result_dict

    except FileNotFoundError:
        print("CSV file not found")
        return {}
    except KeyError as e:
        print(f"Column not found: {e}")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

# Example usage:
if __name__ == "__main__":
    employee_id = "EMP001"
    employee_data = get_personal_employee_info(employee_id)
    if employee_data:
        print(f"Employee {employee_id} data:")
        for key, value in employee_data.items():
            print(f"{key}: {value}")

    payment_data = get_payment_employee_info(employee_id)
    if payment_data:
        print(f"Payment info for {employee_id}:")
        for key, value in payment_data.items():
            print(f"{key}: {value}")
    else:
        print("No data retrieved")
