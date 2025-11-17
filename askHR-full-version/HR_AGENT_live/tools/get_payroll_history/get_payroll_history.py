from ibm_watsonx_orchestrate.agent_builder.tools import tool
import pandas as pd

@tool
def get_payroll_history(employee_id: str) -> dict:
    """
    Returns payroll history data for a specified employee as a dictionary. The returned message includes: 
    payroll_id, employee_id, pay_period_start, pay_period_end, pay_date, gross_pay, withholding_tax, 
    social_security_deduction, net_pay, ytd_gross, ytd_withholding_tax, and slip_file_path.
    One employee can have more than one payroll record.

    Summary of Payroll History Data:
        - payroll_id: Unique identifier for each payroll record.
        - employee_id: Identifier for the employee associated with the payroll record.
        - pay_period_start: Start date of the pay period.
        - pay_period_end: End date of the pay period.
        - pay_date: Date the payment was made.
        - gross_pay: Total earnings before deductions (in THB).
        - withholding_tax: Amount of income tax withheld (in THB).
        - social_security_deduction: Amount of social security contribution (in THB).
        - net_pay: Total earnings after deductions (in THB).
        - ytd_gross: Year-to-date gross earnings (in THB).
        - ytd_withholding_tax: Year-to-date withholding tax (in THB).
        - slip_file_path: URL or file path to the digital pay slip document.

    Args:
        employee_id (str): Employee ID to look up (case-insensitive).

    Returns:
        dict: Dictionary with column headers as keys and row values as values.
              Returns an empty dict if the employee is not found.
    """
    try:
        # This DataFrame contains mock payroll data for employees in Thailand (THB).
        # The withholding tax and net pay are approximations for realism.
        df = pd.DataFrame({
            'payroll_id': ['PR2025001', 'PR2025002', 'PR2025003', 'PR2025004', 'PR2025005', 'PR2024001', 'PR2024002', 'PR2024003', 'PR2024004', 'PR2024005'],
            'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005', 'EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005'],
            'pay_period_start': ['2025-07-01', '2025-07-01', '2025-07-01', '2025-07-01', '2025-07-01', '2025-06-01', '2025-06-01', '2025-06-01', '2025-06-01', '2025-06-01'],
            'pay_period_end': ['2025-07-31', '2025-07-31', '2025-07-31', '2025-07-31', '2025-07-31', '2025-06-30', '2025-06-30', '2025-06-30', '2025-06-30', '2025-06-30'],
            'pay_date': ['2025-07-28', '2025-07-28', '2025-07-28', '2025-07-28', '2025-07-28', '2025-06-27', '2025-06-27', '2025-06-27', '2025-06-27', '2025-06-27'],
            'gross_pay': [95000, 78000, 68000, 72000, 58000, 95000, 78000, 68000, 72000, 58000],
            'withholding_tax': [11063, 7367, 5379, 6167, 3879, 11063, 7367, 5379, 6167, 3879],
            'social_security_deduction': [750, 750, 750, 750, 750, 750, 750, 750, 750, 750],
            'net_pay': [83187, 69883, 61871, 65083, 53371, 83187, 69883, 61871, 65083, 53371],
            'ytd_gross': [665000, 546000, 476000, 504000, 406000, 570000, 468000, 408000, 432000, 348000],
            'ytd_withholding_tax': [77441, 51569, 37653, 43169, 27153, 66378, 44202, 32274, 37002, 23274],
            'slip_file_path': [
                'https://s3.jp-tok.cloud-object-storage.appdomain.cloud/mock-hr-doc/Payslip%20Template%20for%20Excel%20and%20Google%20Sheets%20%281%29.png',
                'https://drive.google.com/file/d/1TeRA066tZw6DsTFC6D86AegaYUC_aiv4/view?usp=sharing',
                'https://drive.google.com/file/d/1TeRA066tZw6DsTFC6D86AegaYUC_aiv4/view?usp=sharing',
                'https://drive.google.com/file/d/1TeRA066tZw6DsTFC6D86AegaYUC_aiv4/view?usp=sharing',
                'https://drive.google.com/file/d/1TeRA066tZw6DsTFC6D86AegaYUC_aiv4/view?usp=sharing',
                'https://drive.google.com/file/d/1TeRA066tZw6DsTFC6D86AegaYUC_aiv4/view?usp=sharing',
                'https://drive.google.com/file/d/1TeRA066tZw6DsTFC6D86AegaYUC_aiv4/view?usp=sharing',
                'https://drive.google.com/file/d/1TeRA066tZw6DsTFC6D86AegaYUC_aiv4/view?usp=sharing',
                'https://drive.google.com/file/d/1TeRA066tZw6DsTFC6D86AegaYUC_aiv4/view?usp=sharing',
                'https://drive.google.com/file/d/1TeRA066tZw6DsTFC6D86AegaYUC_aiv4/view?usp=sharing'
            ]
        })

        # Case-insensitive match for employee_id
        mask = df['employee_id'].str.lower() == employee_id.lower()
        filtered_df = df[mask]

        # Check if any rows match
        if filtered_df.empty:
            print(f"No employee with ID {employee_id} found")
            return {}

        # Convert the matching rows to a dictionary
        result_dict = filtered_df.to_dict(orient='list')

        return result_dict

    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

# Example usage:
if __name__ == "__main__":
    employee_id_to_check = "EMP001"
    employee_data = get_payroll_history(employee_id_to_check)
    if employee_data:
        print(f"Payroll history for {employee_id_to_check}:")
        # Format the output for better readability
        df_result = pd.DataFrame(employee_data)
        print(df_result.to_string())
    else:
        print("No data retrieved")
