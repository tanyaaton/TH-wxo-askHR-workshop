from ibm_watsonx_orchestrate.agent_builder.tools import tool
import pandas as pd

def get_employee_data_source():
    """Returns a pandas DataFrame with mock employee data."""
    data = {
        'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005', 'EMP006'],
        'job_title': ['Senior Software Engineer', 'Marketing Manager', 'Financial Analyst', 'HR Specialist', 'Ops Coordinator', 'Sales Executive'],
        'base_salary': [95000, 78000, 68000, 72000, 58000, 58333.33], # Monthly salary in THB
        'tax_filing_status': ['Single', 'Single', 'Single', 'Single', 'Single', 'Single'],
        'retirement_401k_percent': [6, 4, 5, 6, 3, 5]
    }
    return pd.DataFrame(data)

@tool
def calculate_tax(employee_id: str) -> dict:
    """
    Calculates the estimated annual Thai personal income tax for an employee.

    It first calculates the gross annual income, then subtracts standard deductions
    (expense deduction and personal deduction) to get the net taxable income,
    and finally applies the progressive tax rates.

    Args:
        employee_id (str): The ID of the employee to calculate tax for.

    Returns:
        dict: A dictionary with the tax calculation breakdown or an error message.
    """
    df = get_employee_data_source()
    emp_id = employee_id.upper()

    employee_data = df[df['employee_id'].str.upper() == emp_id]

    if employee_data.empty:
        return {"status": "Error", "message": f"Employee ID {employee_id} not found."}

    details = employee_data.iloc[0]
    monthly_salary = details['base_salary']
    
    annual_income = monthly_salary * 12

    # Standard expense deduction at 50%, capped at 100,000 THB
    expense_deduction = min(annual_income * 0.5, 100000)

    personal_deduction = 60000
    
    total_deductions = personal_deduction + expense_deduction
    net_taxable_income = annual_income - total_deductions
    
    if net_taxable_income < 0:
        net_taxable_income = 0

    total_tax = 0
    if net_taxable_income <= 150000:
        total_tax = 0
    elif net_taxable_income <= 300000:
        total_tax = (net_taxable_income - 150000) * 0.05
    elif net_taxable_income <= 500000:
        total_tax = 7500 + (net_taxable_income - 300000) * 0.10
    elif net_taxable_income <= 750000:
        total_tax = 27500 + (net_taxable_income - 500000) * 0.15
    elif net_taxable_income <= 1000000:
        total_tax = 65000 + (net_taxable_income - 750000) * 0.20
    elif net_taxable_income <= 2000000:
        total_tax = 115000 + (net_taxable_income - 1000000) * 0.25
    elif net_taxable_income <= 5000000:
        total_tax = 365000 + (net_taxable_income - 2000000) * 0.30
    else:
        total_tax = 1265000 + (net_taxable_income - 5000000) * 0.35

    net_annual_income = annual_income - total_tax

    return {
        "status": "Success",
        "employee_id": emp_id,
        "annual_income_thb": f"{annual_income:,.2f}",
        "total_deductions_thb": f"{total_deductions:,.2f}",
        "net_taxable_income_thb": f"{net_taxable_income:,.2f}",
        "annual_tax_liability_thb": f"{total_tax:,.2f}",
        "net_annual_income_thb": f"{net_annual_income:,.2f}",
        "note": "เป็นการคำนวณเบื้องต้นโดยหักค่าใช้จ่าย 50% (สูงสุด 100,000 บาท) และค่าลดหย่อนส่วนตัว 60,000 บาทแล้ว แต่ยังไม่ได้รวมค่าลดหย่อนอื่นๆ"
    }