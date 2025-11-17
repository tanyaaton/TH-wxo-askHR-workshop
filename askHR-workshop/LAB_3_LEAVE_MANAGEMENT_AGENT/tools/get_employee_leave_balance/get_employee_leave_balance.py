from ibm_watsonx_orchestrate.agent_builder.tools import tool
import pandas as pd

@tool
def get_employee_leave_balance(employee_id: str) -> dict:
    """
    Retrieves leave balance information for a specified employee (case-insensitive) from a CSV file (mocked as a DataFrame).

    Summary of Leave Balance Data:
        - Annual leave (total, used, available)
        - Sick leave (total, used, available)
        - Personal leave (total, used, available)
        - Floating holidays (total, used, available)
        - Bereavement leave available
        - Jury duty leave available
        - Last updated date

    Args:
        employee_id (str): Employee ID to look up (case-insensitive, e.g., 'EMP001').

    Returns:
        dict: Dictionary with leave balance details for an employee, or empty dict if not found.
    """
    try:
        # Read the CSV file
        # df = pd.read_csv('employee_leave_balances.csv')  # Replace with your actual CSV filename
        df = pd.DataFrame({
            'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005'],
            'leave_year': [2025, 2025, 2025, 2025, 2025],
            'annual_leave_total': [20, 25, 20, 15, 22],
            'annual_leave_used': [8, 5, 0, 3, 3],
            'annual_leave_available': [12, 20, 20, 12, 19],
            'sick_leave_total': [10, 10, 10, 10, 10],
            'sick_leave_used': [2, 0, 0, 1, 3],
            'sick_leave_available': [8, 10, 10, 9, 7],
            'personal_leave_total': [5, 5, 5, 5, 5],
            'personal_leave_used': [1, 0, 0, 0, 1],
            'personal_leave_available': [4, 5, 5, 5, 4],
            'last_updated': ['2025-10-01', '2025-10-01', '2025-10-01', '2025-10-01', '2025-10-01']
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
    employee_data = get_employee_leave_balance(employee_id)
    if employee_data:
        print("Employee EMP001 data:")
        for key, value in employee_data.items():
            print(f"{key}: {value}")
    else:
        print("No data retrieved")
