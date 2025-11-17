from ibm_watsonx_orchestrate.agent_builder.tools import tool
import pandas as pd

@tool
def get_salary_certificate(employee_id: str) -> dict:
    """
    Generates and returns a link to the salary certificate PDF for a specified employee.

    This tool verifies an employee by their ID and creates a downloadable link to their salary certificate.

    Args:
        employee_id (str): The unique identifier for the employee to look up (e.g., 'EMP001'). This is case-insensitive.

    Returns:
        dict: A dictionary with the key 'certificate_link' and the URL to the PDF file as the value.
              Returns an empty dictionary if the employee is not found.
    """
    try:
        # Mock DataFrame to verify employee existence.
        # In a real scenario, this would connect to a database or a file.
        df = pd.DataFrame({
            'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005']
        })

        # Case-insensitive search for the employee_id
        mask = df['employee_id'].str.lower() == employee_id.lower()
        employee_found = not df[mask].empty

        # Check if the employee was found
        if not employee_found:
            print(f"No employee with ID {employee_id} found")
            return {}

        # Generate a unique, consistent link for the employee's certificate
        # Using .upper() to ensure consistency in the generated URL
        link = "https://drive.google.com/file/d/1RkqN-N2_VUYtDkDGaH3bQ8cn7Qxqy_Uw/view?usp=sharing"
        
        result_dict = {"certificate_link": link}

        return result_dict

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}
