from ibm_watsonx_orchestrate.agent_builder.tools import tool
import pandas as pd

# This mock data source simulates a database of employee compensation details.
# It is defined here to be accessible by both tools.
# NOTE: We assume all employees are in the private sector for this demo.
def get_employee_data_source():
    """Returns a pandas DataFrame with mock employee data."""
    data = {
        'employee_id': ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005'],
        'job_title': ['Senior Software Engineer', 'Marketing Manager', 'Financial Analyst', 'HR Specialist', 'Ops Coordinator'],
        # Represents monthly salary in THB
        'base_salary': [95000, 78000, 45000, 72000, 28000],
        'tax_filing_status': ['Single', 'Single', 'Single', 'Single', 'Single'],
        # Represents Provident Fund contribution percentage
        'retirement_401k_percent': [10, 5, 8, 4, 3]
    }
    return pd.DataFrame(data)

@tool
def recommendation(employee_id: str) -> dict:
    """
    Provides tax-saving fund recommendations for an employee in Thailand
    based on their annual income level.

    This tool analyzes the employee's salary to suggest appropriate funds like
    Provident Fund, RMF, and Thai ESG to reduce their tax burden for the year 2025 (2568 BE).

    Args:
        employee_id (str): The ID of the employee to get recommendations for.

    Returns:
        dict: A dictionary containing a list of recommendations or an error message.
    """
    df = get_employee_data_source()
    emp_id = employee_id.upper()

    employee_data = df[df['employee_id'].str.upper() == emp_id]

    if employee_data.empty:
        return {"status": "Error", "message": f"Employee ID {employee_id} not found."}

    details = employee_data.iloc[0]
    monthly_salary = details['base_salary']
    provident_fund_percent = details['retirement_401k_percent']
    
    # Calculate annual income to determine the recommendation strategy
    annual_income = monthly_salary * 12
    
    recs = []

    # --- Recommendation Logic based on Annual Income Tiers ---

    # Standard recommendations for everyone
    recs.append(f"**กองทุนประกันสังคม (Social Security Fund):** คุณได้ใช้สิทธิลดหย่อนจากส่วนนี้อยู่แล้ว ซึ่งเป็นข้อบังคับพื้นฐาน")
    
    # Provident Fund is a great starting point.
    if provident_fund_percent < 15: # Max contribution is 15%
        recs.append(f"**กองทุนสำรองเลี้ยงชีพ (Provident Fund):** ปัจจุบันคุณสะสมอยู่ {provident_fund_percent}%. "
                    "แนะนำให้พิจารณาเพิ่มเงินสะสมให้สูงขึ้น (สูงสุด 15%) เนื่องจากเป็นวิธีลดหย่อนภาษีที่คุ้มค่า "
                    "เพราะจะได้รับเงินสมทบจากนายจ้างเพิ่มด้วย")
    else:
        recs.append(f"**กองทุนสำรองเลี้ยงชีพ (Provident Fund):** ยอดเยี่ยมมาก! คุณสะสมในระดับที่ดีแล้ว ({provident_fund_percent}%) "
                    "ซึ่งช่วยลดหย่อนภาษีได้อย่างมีประสิทธิภาพ")

    # Tier 1: Low-Mid Income (Annual Income < 600,000 THB)
    # Focus on fundamental savings, tax benefit is a bonus.
    if annual_income < 600000:
        recs.append("**คำแนะนำเพิ่มเติม:** ในระดับรายได้นี้ การเน้นที่กองทุนสำรองเลี้ยงชีพเป็นสิ่งสำคัญที่สุด "
                    "หากยังมีกำลังเหลือ สามารถพิจารณา **Thai ESG** เพื่อเริ่มสร้างวินัยการลงทุนระยะยาวและลดหย่อนภาษีเพิ่มเติมได้")

    # Tier 2: Mid-High Income (600,000 <= Annual Income < 1,200,000 THB)
    # Tax burden is becoming significant. RMF and Thai ESG are highly recommended.
    elif annual_income < 1200000:
        recs.append("**กองทุน Thai ESG:** เพื่อลดหย่อนภาษีเพิ่มเติมและส่งเสริมการลงทุนอย่างยั่งยืน (ถือครอง 5 ปี) "
                    "คุณสามารถลงทุนได้สูงสุด 30% ของเงินได้ แต่ไม่เกิน 300,000 บาท")
        recs.append("**กองทุน RMF (Retirement Mutual Fund):** หากต้องการวางแผนเกษียณอย่างจริงจัง RMF เป็นตัวเลือกที่ยอดเยี่ยม "
                    "สามารถลดหย่อนภาษีได้สูงสุด 30% ของเงินได้ แต่ไม่เกิน 500,000 บาท (เมื่อรวมกับกองทุนสำรองเลี้ยงชีพและกองทุนเพื่อการเกษียณอื่นๆ) "
                    "และต้องลงทุนต่อเนื่องถึงอายุ 55 ปี")
        
    # Tier 3: High Income (Annual Income >= 1,200,000 THB)
    # Should maximize all available tax-deductible funds.
    else:
        recs.append("**Maximise Tax Savings:** ในระดับรายได้ของคุณ การลดหย่อนภาษีจะช่วยประหยัดเงินได้มาก "
                    "แนะนำให้ใช้สิทธิลดหย่อนให้เต็มเพดาน")
        recs.append("**กองทุน RMF:** เป็นเครื่องมือสำคัญในการวางแผนเกษียณและลดหย่อนภาษีก้อนใหญ่ "
                    "สามารถลดหย่อนได้สูงสุด 30% ของเงินได้ ไม่เกิน 500,000 บาท (เมื่อรวมกับกองทุนสำรองเลี้ยงชีพและกองทุนเพื่อการเกษียณอื่นๆ)")
        recs.append("**กองทุน Thai ESG:** เป็นอีกหนึ่งทางเลือกที่ยอดเยี่ยมในการลดหย่อนภาษีเพิ่มเติม "
                    "สามารถลงทุนได้สูงสุด 30% ของเงินได้ แต่ไม่เกิน 300,000 บาท โดยเป็นวงเงินแยกต่างหากจาก RMF")

    return {
        "status": "Success",
        "employee_id": emp_id,
        "annual_income_thb": f"{annual_income:,.2f}",
        "recommendations": recs
    }