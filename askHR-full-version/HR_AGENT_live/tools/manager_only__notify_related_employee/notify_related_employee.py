import pandas as pd
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def manager_only__notify_related_employee(employee_id: str, message: str, notification_type: str = "general") -> str:
    """
    Send notifications to employees about HR matters affecting them. Only user with {employee_role} ="manager" can access this tool

    
    Args:
        employee_id (str): Employee ID to notify
        message (str): Notification message
        notification_type (str): Type of notification (leave_approval, leave_denial, team_schedule, policy_reminder, general)
        
    Returns:
        str: Confirmation of notification sent
    """
    try:
        # Mock employee data with manager relationships
        emp_data = pd.DataFrame({
            'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005', 'EMP006'],
            'first_name': ['John', 'Jane', 'Mike', 'Sarah', 'David', 'Lisa'],
            'last_name': ['Smith', 'Johnson', 'Brown', 'Davis', 'Wilson', 'Miller'],
            'manager_id': ['MGR001', 'MGR001', 'MGR001', 'MGR001', 'MGR001', 'MGR002'],
            'email': ['john.smith@company.com', 'jane.johnson@company.com', 'mike.brown@company.com', 
                     'sarah.davis@company.com', 'david.wilson@company.com', 'lisa.miller@company.com']
        })
        
        # Find employee information
        employee_info = emp_data[emp_data['employee_id'] == employee_id]
        
        if employee_info.empty:
            return f"Employee {employee_id} not found"
        
        # Verify manager authority (assuming current manager context)
        current_manager = 'MGR001'
        if employee_info['manager_id'].iloc[0].lower() != current_manager.lower():
            return f"Access denied. You cannot send notifications to employee {employee_id} as they are not your direct report"
        
        # Mock notification details
        employee_name = employee_info['first_name'].iloc[0] + " " + employee_info['last_name'].iloc[0]
        employee_email = employee_info['email'].iloc[0]
        current_date = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Different notification formats based on type
        notification_formats = {
            'leave_approval': f"LEAVE APPROVED",
            'leave_denial': f"LEAVE DENIED", 
            'team_schedule': f"TEAM SCHEDULE UPDATE",
            'policy_reminder': f"POLICY REMINDER",
            'general': f"GENERAL NOTIFICATION"
        }
        
        notification_header = notification_formats.get(notification_type, notification_formats['general'])
        
        # Mock sending notification (in real implementation, this would send actual email/message)
        notification_details = f"""
{notification_header}

To: {employee_name} ({employee_email})
From: Manager (MGR001)
Date: {current_date}
Type: {notification_type}

Message:
{message}

---
This notification has been sent successfully via:
✓ Email notification
✓ Internal messaging system
✓ Mobile app push notification

Status: DELIVERED
        """
        
        return f"Notification sent successfully to {employee_name} ({employee_id}):\n{notification_details.strip()}"
        
    except Exception as e:
        return f"Error sending notification: {str(e)}"
