import pandas as pd
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def manager_only__get_all_employee_leave_balance(employee_role: str) -> str:
    """
    Get leave balances for all employees in your team. Only user with {employee_role} ="manager" can access this tool

    Args:
        employee_role (str): Role of the user attempting to view team's leave balances

    Returns:
        str: Leave balances for all team members
    """
    if employee_role.lower() != 'manager':
        return "Access denied. Only managers can view team leave balances."
    try:
        # Mock employee data with manager relationships
        emp_data = pd.DataFrame({
            'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005', 'EMP006'],
            'first_name': ['John', 'Jane', 'Mike', 'Sarah', 'David', 'Lisa'],
            'last_name': ['Smith', 'Johnson', 'Brown', 'Davis', 'Wilson', 'Miller'],
            'manager_id': ['MGR001', 'MGR001', 'MGR001', 'MGR001', 'MGR002', 'MGR002']
        })
        
        # Mock leave balances data
        leave_data = pd.DataFrame({
            'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005', 'EMP006'],
            'annual_leave': [15, 20, 18, 12, 25, 10],
            'sick_leave': [8, 10, 9, 7, 10, 6],
            'personal_leave': [3, 5, 4, 2, 5, 3],
            'total_used': [7, 5, 2, 8, 0, 14],
            'last_updated': ['2025-10-01', '2025-10-01', '2025-09-28', '2025-10-05', '2025-10-01', '2025-09-30']
        })
        
        # Get all team employees (assuming manager context is already established)
        # For demo purposes, showing team under MGR001
        current_manager = 'MGR001'
        team_employees = emp_data[emp_data['manager_id'].str.lower() == current_manager.lower()]
        employee_ids = team_employees['employee_id'].tolist()
        
        if not employee_ids:
            return f"No employees found in your team"
        
        # Filter leave balances for team members
        team_balances = leave_data[leave_data['employee_id'].isin(employee_ids)]
        
        if team_balances.empty:
            return f"No leave balance data found for your team"
        
        # Add employee names and format results
        results = []
        for _, balance in team_balances.iterrows():
            employee_info = team_employees[team_employees['employee_id'] == balance['employee_id']]
            if not employee_info.empty:
                employee_name = employee_info['first_name'].iloc[0] + " " + employee_info['last_name'].iloc[0]
                
                results.append({
                    'Employee': employee_name,
                    'Employee_ID': balance['employee_id'],
                    'Annual_Leave': balance['annual_leave'],
                    'Sick_Leave': balance['sick_leave'],
                    'Personal_Leave': balance['personal_leave'],
                    'Total_Used': balance['total_used'],
                    'Last_Updated': balance['last_updated']
                })
        
        return f"Leave balances for your team:{pd.DataFrame(results).to_string(index=False)}"
        
    except Exception as e:
        return f"Error retrieving leave balances: {str(e)}"
