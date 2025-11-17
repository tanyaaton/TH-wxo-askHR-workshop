from ibm_watsonx_orchestrate.agent_builder.tools import tool
import pandas as pd

@tool
def get_tax_document(employee_id: str) -> dict:
    """
    Returns tax document data for a specified employee as a dictionary. The returned message includes: employee_id, tax_year, document_type, document_file_path, and issue_date.

    Summary of tax document data:
        - document_id: Unique identifier for each tax document.
        - employee_id: Identifier for the employee associated with the tax document.
        - document_type: Type of tax document (e.g., W-2).
        - tax_year: The tax year the document pertains to.
        - issue_date: Date the document was issued.
        - file_path: Location where the document is stored.
        - document_status: Current status of the document (e.g., Available).
        - total_wages: Total wages reported on the tax document.
        - federal_tax_withheld: Amount of federal tax withheld.
        - state_tax_withheld: Amount of state tax withheld.
        - social_security_wages: Wages subject to Social Security tax.
        - medicare_wages: Wages subject to Medicare tax.
        - retirement_contributions: Amount contributed to retirement plans.

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
            'document_id': ['TAX2024001', 'TAX2024002', 'TAX2024003', 'TAX2024004', 'TAX2024005', 'TAX2023001', 'TAX2023002', 'TAX2023003', 'TAX2023004', 'TAX2023005'],
            'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005', 'EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005'],
            'document_type': ['W-2', 'W-2', 'W-2', 'W-2', 'W-2', 'W-2', 'W-2', 'W-2', 'W-2', 'W-2'],
            'tax_year': [2024, 2024, 2024, 2024, 2024, 2023, 2023, 2023, 2023, 2023],
            'issue_date': ['2025-01-31', '2025-01-31', '2025-01-31', '2025-01-31', '2025-01-31', '2024-01-31', '2024-01-31', '2024-01-31', '2024-01-31', '2024-01-31'],
            'file_path': [
                'https://drive.google.com/file/d/1j41VQvOXebpHeRkKAAAYwZiuTCxFoQxb/view?usp=sharing',
                'https://drive.google.com/file/d/1j41VQvOXebpHeRkKAAAYwZiuTCxFoQxb/view?usp=sharing',
                'https://drive.google.com/file/d/1j41VQvOXebpHeRkKAAAYwZiuTCxFoQxb/view?usp=sharing',
                'https://drive.google.com/file/d/1j41VQvOXebpHeRkKAAAYwZiuTCxFoQxb/view?usp=sharing',
                'https://drive.google.com/file/d/1j41VQvOXebpHeRkKAAAYwZiuTCxFoQxb/view?usp=sharing',
                'https://drive.google.com/file/d/1j41VQvOXebpHeRkKAAAYwZiuTCxFoQxb/view?usp=sharing',
                'https://drive.google.com/file/d/1j41VQvOXebpHeRkKAAAYwZiuTCxFoQxb/view?usp=sharing',
                'https://drive.google.com/file/d/1j41VQvOXebpHeRkKAAAYwZiuTCxFoQxb/view?usp=sharing',
                'https://drive.google.com/file/d/1j41VQvOXebpHeRkKAAAYwZiuTCxFoQxb/view?usp=sharing',
                'https://drive.google.com/file/d/1j41VQvOXebpHeRkKAAAYwZiuTCxFoQxb/view?usp=sharing'
            ],
            'document_status': ['Available', 'Available', 'Available', 'Available', 'Available', 'Available', 'Available', 'Available', 'Available', 'Available'],
            'total_wages': [95000, 78000, 68000, 72000, 58000, 92000, 75000, 65000, 70000, 56000],
            'federal_tax_withheld': [14262, 9360, 8160, 8640, 5800, 13800, 9000, 7800, 8400, 5600],
            'state_tax_withheld': [3800, 2730, 2380, 2520, 2030, 3680, 2625, 2275, 2450, 1960],
            'social_security_wages': [95000, 78000, 68000, 72000, 58000, 92000, 75000, 65000, 70000, 56000],
            'medicare_wages': [95000, 78000, 68000, 72000, 58000, 92000, 75000, 65000, 70000, 56000],
            'retirement_contributions': [11400, 6760, 7396, 9360, 3770, 11040, 6500, 7150, 9100, 3640]
        })

        # Case-insensitive match for employee_id
        mask = df['employee_id'].str.lower() == employee_id.lower()
        filtered_df = df[mask]

        # Check if any rows match
        if filtered_df.empty:
            print(f"No employee with ID {employee_id} found")
            return {}

        # Convert the matching rows to dictionary (all tax documents for the employee)
        result_dict = filtered_df.to_dict(orient='list')

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
    employee_data = get_tax_document(employee_id)
    if employee_data:
        print(f"Tax documents for {employee_id}:")
        for key, value in employee_data.items():
            print(f"{key}: {value}")
    else:
        print("No data retrieved")
