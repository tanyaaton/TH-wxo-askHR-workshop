from ibm_watsonx_orchestrate.agent_builder.tools import tool
import pandas as pd

@tool
def get_employee_compensation(employee_id: str) -> dict:
    """
    Returns compensation and salary data for a specified employee as a dictionary. The returned message includes: employee_id, job_title, salary_type, base_salary, pay_frequency, bank_account_number, tax_filing_status, health_insurance_deduction, retirement_401k_percent, and effective_date.

    Summary of Compensation Data:
        - employee_id: Identifier for the employee.
        - job_title: The employee's job title.
        - salary_type: Type of salary (e.g., Salary, Hourly).
        - base_salary: The base salary amount.
        - pay_frequency: Frequency of salary payment (e.g., Monthly, Bi-Weekly).
        - bank_account_number: Masked bank account number for direct deposit.
        - tax_filing_status: Employee's tax filing status (e.g., Single, Married Filing Jointly).
        - health_insurance_deduction: Monthly deduction amount for health insurance.
        - retirement_401k_percent: Percentage of salary contributed to 401(k) retirement plan.
        - effective_date: Date when the current compensation details became effective.

    Args:
        employee_id (str): Employee ID to look up (case-insensitive).

    Returns:
        dict: Dictionary with column headers as keys and row values as values.
              Returns empty dict if employee not found.
    """
    try:
        # Read the CSV file
        # df = pd.read_csv('employee_personal_info.csv')  # Replace with your actual CSV filename
        df = pd.DataFrame({
            'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005'],
            'job_title': ['Senior Software Engineer', 'Marketing Manager', 'Financial Analyst', 'HR Specialist', 'Operations Coordinator'],
            'salary_type': ['Salary', 'Salary', 'Salary', 'Salary', 'Salary'],
            'base_salary': [95000, 78000, 68000, 72000, 58000],
            'pay_frequency': ['Monthly', 'Monthly', 'Monthly', 'Monthly', 'Monthly'],
            'bank_account_number': ['****1234', '****5678', '****9012', '****3456', '****7890'],
            'tax_filing_status': ['Married Filing Jointly', 'Single', 'Married Filing Jointly', 'Head of Household', 'Single'],
            'health_insurance_deduction': [450, 250, 450, 450, 250],
            'retirement_401k_percent': [6, 4, 5, 6, 3],
            'effective_date': ['2022-03-15', '2021-07-01', '2023-01-10', '2020-05-20', '2019-11-08']
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
    employee_data = get_employee_compensation(employee_id)
    if employee_data:
        print(f"Employee {employee_id} data:")
        for key, value in employee_data.items():
            print(f"{key}: {value}")
    else:
        print("No data retrieved")
