from ibm_watsonx_orchestrate.agent_builder.tools import tool
import pandas as pd

@tool 
def get_leave_request(employee_id: str) -> dict:
    """
    Returns all leave request records for a specified employee as a dictionary (case-insensitive).

    Summary of Leave Request Data:
        - Each request includes: leave_request_id, employee_id, leave_type, start_date, end_date, days_requested, status, request_date, approved_by, approval_date, notes.
        - Multiple requests per employee are possible; all requests for the given employee are returned.
        - Data is returned as a dictionary with column headers as keys and lists of values for an employee.
        - If no requests are found for an employee, returns an empty dictionary.

    Args:
        employee_id (str): Employee ID to look up (case-insensitive).

    Returns:
        dict: Dictionary with leave request details for the employee, or empty dict if not found.
    """
    df = pd.DataFrame({
        'leave_request_id': ['LR001', 'LR002', 'LR003', 'LR004', 'LR005', 'LR006', 'LR007', 'LR008', 'LR009', 'LR010'],
        'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP001', 'EMP004', 'EMP005', 'EMP002', 'EMP003', 'EMP001', 'EMP005'],
        'leave_type': ['Annual Leave', 'Sick Leave', 'Annual Leave', 'Personal Leave', 'Annual Leave', 'Sick Leave', 'Annual Leave', 'Bereavement Leave', 'Annual Leave', 'Personal Leave'],
        'start_date': ['2024-12-20', '2025-01-15', '2025-02-10', '2025-03-05', '2025-06-15', '2024-11-10', '2025-04-07', '2024-09-20', '2025-07-01', '2025-01-30'],
        'end_date': ['2024-12-24', '2025-01-16', '2025-02-14', '2025-03-05', '2025-06-29', '2024-11-12', '2025-04-11', '2024-09-24', '2025-07-05', '2025-01-30'],
        'days_requested': [3, 2, 5, 1, 10, 3, 5, 5, 5, 1],
        'status': ['Approved', 'Approved', 'Pending', 'Approved', 'Pending', 'Approved', 'Approved', 'Approved', 'Pending', 'Approved'],
        'request_date': ['2024-11-15', '2025-01-14', '2025-01-25', '2025-02-20', '2025-05-15', '2024-11-09', '2025-03-10', '2024-09-19', '2025-06-01', '2025-01-20'],
        'approved_by': ['Sarah Johnson', 'Michael Chen', '', 'Sarah Johnson', '', 'Robert Kim', 'Michael Chen', 'Lisa Park', '', 'Robert Kim'],
        'approval_date': ['2024-11-17', '2025-01-14', '', '2025-02-22', '', '2024-11-09', '2025-03-12', '2024-09-19', '', '2025-01-21'],
        'notes': ['Christmas vacation', 'Flu symptoms', "Valentine's week vacation", 'Doctor appointment', 'Summer vacation - Europe', 'Back injury recovery', 'Spring break with family', "Grandmother's passing", '4th of July week', 'DMV appointment']
    })

    # Case-insensitive match for employee_id
    mask = df['employee_id'].str.lower() == employee_id.lower()
    filtered_df = df[mask]

    # Check if any rows match
    if filtered_df.empty:
        print(f"No leave request for employee ID {employee_id} found")
        return {}

    # Convert the matching rows to dictionary
    result_dict = filtered_df.to_dict(orient='list')

    return result_dict

# Example usage:
if __name__ == "__main__":
    employee_id = "EMP001"
    leave_request_data = get_leave_request(employee_id)
    if leave_request_data:
        print(f"Leave request data for employee {employee_id}:")
        for key, value in leave_request_data.items():
            print(f"{key}: {value}")
    else:
        print("No leave request data retrieved")
