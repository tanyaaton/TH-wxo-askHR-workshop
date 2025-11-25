import pandas as pd
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def manager_only__view_all_leave_requests(employee_role: str) -> str:
    """
    View all leave requests for employees in your team. Only user with {employee_role} ="manager" can access this tool
    
    Args:
        employee_role (str): Role of the user attempting to view team's leave requests

    Returns:
        str: List of all leave requests for your team
    """
    if employee_role.lower() != 'manager':
        return "Access denied. Only managers can view team leave requests."
    try:
        # Mock employee data with manager relationships
        emp_data = pd.DataFrame({
            'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005', 'EMP006'],
            'first_name': ['John', 'Jane', 'Mike', 'Sarah', 'David', 'Lisa'],
            'last_name': ['Smith', 'Johnson', 'Brown', 'Davis', 'Wilson', 'Miller'],
            'manager_id': ['MGR001', 'MGR001', 'MGR001', 'MGR001', 'MGR001', 'MGR002']
        })
        
        # Mock leave requests data
        leave_requests = pd.DataFrame({
            'employee_id': ['EMP001', 'EMP002', 'EMP001', 'EMP004', 'EMP003', 'EMP005'],
            'request_id': ['REQ001', 'REQ002', 'REQ003', 'REQ004', 'REQ005', 'REQ006'],
            'leave_type': ['Annual', 'Sick', 'Personal', 'Annual', 'Annual', 'Sick'],
            'start_date': ['2025-10-20', '2025-10-15', '2025-11-01', '2025-10-25', '2025-11-10', '2025-10-18'],
            'end_date': ['2025-10-22', '2025-10-15', '2025-11-05', '2025-10-27', '2025-11-12', '2025-10-20'],
            'status': ['pending', 'approved', 'pending', 'pending', 'approved', 'denied'],
            'reason': ['Family vacation', 'Medical appointment', 'Personal matters', 'Conference attendance', 'Wedding', 'Not urgent']
        })
        
        # Get all team employees (assuming manager context is already established)
        # For demo purposes, showing team under MGR001
        current_manager = 'MGR001'
        team_employees = emp_data[emp_data['manager_id'].str.lower() == current_manager.lower()]
        employee_ids = team_employees['employee_id'].tolist()
        
        if not employee_ids:
            return f"No employees found in your team"
        
        # Filter leave requests for team members
        team_requests = leave_requests[leave_requests['employee_id'].isin(employee_ids)]
        
        if team_requests.empty:
            return f"No leave requests found for your team"
        
        # Format the results
        results = []
        for _, request in team_requests.iterrows():
            employee_info = team_employees[team_employees['employee_id'] == request['employee_id']]
            if not employee_info.empty:
                employee_name = employee_info['first_name'].iloc[0] + " " + employee_info['last_name'].iloc[0]
                
                results.append({
                    'Employee': employee_name,
                    'Employee_ID': request['employee_id'],
                    'Request_ID': request['request_id'],
                    'Leave_Type': request['leave_type'],
                    'Start_Date': request['start_date'],
                    'End_Date': request['end_date'],
                    'Status': request['status'],
                    'Reason': request['reason']
                })
        
        return f"Leave requests for your team:{pd.DataFrame(results).to_string(index=False)}"
        
    except Exception as e:
        return f"Error retrieving leave requests: {str(e)}"
