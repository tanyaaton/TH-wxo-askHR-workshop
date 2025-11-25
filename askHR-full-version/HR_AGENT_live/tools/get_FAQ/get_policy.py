# import PyPDF2
# import pdfplumber
from ibm_watsonx_orchestrate.agent_builder.tools import tool


# def extract_text_from_pdf(pdf_path):
#     """
#     Extracts text from entire PDF file and returns as string
    
#     Args:
#         pdf_path (str): Path to the PDF file
    
#     Returns:
#         str: Extracted text from all pages, empty string if failed
#     """
#     try:
#         text = ""
        
#         # Method 1: Using PyPDF2 (basic extraction)
#         with open(pdf_path, 'rb') as file:
#             pdf_reader = PyPDF2.PdfReader(file)
            
#             for page_num in range(len(pdf_reader.pages)):
#                 page = pdf_reader.pages[page_num]
#                 text += page.extract_text() + "\n"
        
#         return text.strip()
        
#     except Exception as e:
#         print(f"Error extracting text with PyPDF2: {e}")
#         return ""

# def extract_text_from_pdf_advanced(pdf_path):
#     """
#     Extracts text from PDF using pdfplumber (better for complex layouts)
    
#     Args:
#         pdf_path (str): Path to the PDF file
    
#     Returns:
#         str: Extracted text from all pages, empty string if failed
#     """
#     try:
#         text = ""
        
#         with pdfplumber.open(pdf_path) as pdf:
#             for page in pdf.pages:
#                 page_text = page.extract_text()
#                 if page_text:
#                     text += page_text + "\n"
        
#         return text.strip()
        
#     except Exception as e:
#         print(f"Error extracting text with pdfplumber: {e}")
#         return ""

# def extract_pdf_text(pdf_path, method="basic"):
#     """
#     Main function to extract text from PDF with method selection
    
#     Args:
#         pdf_path (str): Path to the PDF file
#         method (str): "basic" for PyPDF2 or "advanced" for pdfplumber
    
#     Returns:
#         str: Extracted text from entire PDF
#     """
#     try:
#         if method == "advanced":
#             return extract_text_from_pdf_advanced(pdf_path)
#         else:
#             return extract_text_from_pdf(pdf_path)
            
#     except FileNotFoundError:
#         print(f"PDF file not found: {pdf_path}")
#         return ""
#     except Exception as e:
#         print(f"Error processing PDF: {e}")
#         return ""

@tool
def get_policy() -> str:
    """
    Tool function to return the HR policy manual as a string.
    This tool does not take any argument.

    Summary of Policy Content:
        - Benefits Plans: Health, dental, vision insurance; retirement (401k); life insurance; FSA; wellness.
        - Leave Rules: PTO accrual, sick leave, holiday leave (dates listed), family leave, leave request process.
        - Probation Policy: Duration, rights, expectations, completion process.
        - Performance Review: Review cycle, rating scale, improvement plans, merit increases, career development.
        - Policy Updates: Annual review and notification process.
        - Contact: HR contact details for questions.

    Returns:
        str: The full text of the HR policy manual.
    """
    # pdf_path = "HR Policy Manual.pdf"  # Replace with your actual PDF file path
    # return extract_pdf_text(pdf_path)
    policy = """TechCorp HR Policy Manual

    Version 2.0 | Effective January 2025
    Table of Contents

    1. Benefits Plans
    2. Leave Rules
    3. Probation Policy
    4. Performance Review Process

    1. BENEFITS PLANS
    Health Insurance

    Medical Coverage: Comprehensive health insurance with 80% company contribution
    Dental Coverage: Full dental coverage with 70% company contribution
    Vision Coverage: Eye care coverage with 60% company contribution
    Eligibility: All full-time employees after 30 days of employment

    Retirement Benefits

    401(k) Plan: Company matches up to 6% of salary
    Vesting Schedule: Immediate vesting for employee contributions, 3-year cliff vesting for company
    match
    Enrollment: Automatic enrollment at 3% contribution rate

    Life Insurance

    Basic Life Insurance: 2x annual salary, company-paid
    Supplemental Life Insurance: Up to 10x salary, employee-paid
    Accidental Death & Dismemberment: Equal to life insurance amount

    Other Benefits

    Flexible Spending Account (FSA): Up to $2,850 for healthcare expenses
    Employee Assistance Program: Free counseling and support services
    Wellness Program: Gym membership reimbursement up to $500/year

    2. LEAVE RULES

    Paid Time Off (PTO)

    Accrual Rate:
    0-2 years: 15 days annually
    3-5 years: 20 days annually
    6+ years: 25 days annually
    Maximum Carryover: 5 days to next calendar year
    Cash Out: Not permitted

    Sick Leave

    Accrual: 1 day per month (12 days annually)
    Maximum Accumulation: 60 days
    Usage: For personal illness or family care


    Holiday Leave

    Company Holidays: 12 paid holidays per year
    Holiday Dates (2025):
        - New Year's Day: January 1
        - Martin Luther King Jr. Day: January 20
        - Presidents' Day: February 17
        - Memorial Day: May 26
        - Independence Day: July 4
        - Labor Day: September 1
        - Columbus Day: October 13
        - Veterans Day: November 11
        - Thanksgiving Day: November 27
        - Day After Thanksgiving: November 28
        - Christmas Eve: December 24
        - Christmas Day: December 25
    Floating Holidays: 2 additional days for personal observance

    Family Leave

    Parental Leave: 12 weeks paid for birth/adoption
    Bereavement Leave: 5 days for immediate family, 3 days for extended family
    Jury Duty: Full pay for duration of service

    Leave Request Process

    1. Submit request through HR portal minimum 2 weeks in advance
    2. Manager approval required
    3. HR notification for leaves >5 consecutive days
    4. Medical documentation required for sick leave >3 days

    3. PROBATION POLICY
    Probationary Period

    Duration: 90 days from start date
    Extension: May be extended up to 180 days with cause
    Review: Formal review at 60 and 90 days

    Probationary Employee Rights

    Benefits: Eligible for all benefits after 30 days
    PTO Accrual: Begins immediately, usage after 60 days
    Training: Full access to company training programs

    Performance Expectations

    Job Performance: Must meet all essential job functions
    Attendance: Maximum 2 unexcused absences
    Conduct: Must adhere to all company policies

    Probation Completion

    Successful Completion: Automatic conversion to regular employment
    Unsuccessful: Employment may be terminated without progressive discipline
    Manager Evaluation: Required written assessment at 90 days

    4. PERFORMANCE REVIEW PROCESS
    Review Cycle

    Annual Reviews: Conducted each January for prior year
    Mid-Year Check-ins: Informal reviews in July
    New Employee Reviews: After probation completion

    Performance Rating Scale

    1. Exceeds Expectations (4.0-5.0): Consistently surpasses goals
    2. Meets Expectations (3.0-3.9): Successfully achieves objectives
    3. Below Expectations (2.0-2.9): Requires improvement
    4. Unsatisfactory (1.0-1.9): Fails to meet minimum standards

    Review Components

    Goal Achievement: 40% of overall rating
    Job Knowledge: 25% of overall rating
    Communication: 20% of overall rating
    Teamwork: 15% of overall rating

    Performance Improvement Plans (PIP)

    Trigger: Rating below 2.5 or specific performance issues
    Duration: 90-day improvement period
    Support: Additional training and resources provided
    Outcome: Improvement required to continue employment

    Merit Increases

    Eligibility: Based on performance rating and budget approval
    Range: 0-8% of base salary
    Effective Date: March 1st following review

    Career Development

    Individual Development Plans: Created during annual review
    Training Budget: $2,000 per employee annually
    Internal Promotions: Preference given to qualified internal candidates

    Policy Updates

    This manual is reviewed annually and updated as needed. Employees will be notified of any changes
    via email and company portal.

    Questions?

    Contact HR at hr@techcorp.com or extension 5555.
    """
    return policy

@tool
def get_FAQ() -> str:
    """
    Tool function to return the company FAQ and workplace guidelines as a string.

    Summary of FAQ Content:
        - Workplace Guidelines: Dress code, acceptable/unacceptable attire, travel policies, expense reimbursement, working hours, remote work, overtime, confidentiality, ethics, business conduct.
        - Company Holidays: List of fixed and floating holidays for 2025, holiday pay policy.
        - Benefits: Eligibility, enrollment, impact of leave on benefits.
        - Time Off: Request process, PTO donation, emergency leave.
        - IT and Equipment: Support, software installation, personal use policy.
        - Performance and Development: Review schedule, training, tuition reimbursement.
        - Contact Information: HR, IT, facilities, employee relations contacts.

    Args:
        None

    Returns:
        str: The full text of the company FAQ and workplace guidelines.
    """
    # pdf_path = "Workplace Guidelines and Company FAQ.pdf"  # Replace with your actual PDF file path
    # return extract_pdf_text(pdf_path)
    fqa = """TechCorp Workplace Guidelines & Company FAQ
    Employee Handbook Supplement | Updated January 2025
    WORKPLACE GUIDELINES
    Dress Code Policy
    Professional Business Casual is the standard dress code for all employees.
    Acceptable Attire:
    Business Casual: Khakis, dress pants, polo shirts, button-down shirts, blouses
    Smart Casual: Dark jeans (no rips/distressing), sweaters, cardigans
    Footwear: Closed-toe shoes, loafers, dress shoes, clean sneakers
    Client Meeting Days: Business professional attire required
    Unacceptable Attire:
    Shorts, flip-flops, tank tops, athletic wear
    Clothing with offensive language or images
    Excessively revealing clothing
    Pajamas or loungewear
    Casual Friday:
    Jeans and casual shirts permitted
    Athletic shoes allowed
    Still maintain professional appearance
    Travel Policies
    Business Travel Authorization
    Pre-approval: All business travel requires manager approval
    Booking: Use designated travel agency or approved booking platform
    Advance Notice: Minimum 2 weeks for domestic, 4 weeks for international
    Expense Reimbursement
    Meals: Per diem rates based on destination
    Domestic: $75/day
    International: $100/day
    Lodging: Reasonable accommodations, prefer company-approved hotels
    Transportation:
    Airfare: Economy class for flights under 6 hours
    Rental Cars: Mid-size or smaller
    Mileage: $0.67/mile for personal vehicle use
    Travel Guidelines
    Receipt Requirements: All expenses over $25 require receipts
    Expense Reports: Submit within 30 days of trip completion
    Travel Insurance: Provided for international travel over 7 days
    Emergency Contact: Notify HR of international travel itineraries
    Company Holidays 2025
    Wednesday, January 1 - New Year's Day
    Wednesday, February 12 - Makha Bucha Day
    Monday, April 7 - Substitution for Chakri Memorial Day (April 6)
    Monday, April 14 - Songkran Festival
    Tuesday, April 15 - Songkran Festival
    Thursday, May 1 - National Labour Day
    Monday, May 5 - Substitution for Coronation Day (May 4)
    Monday, May 12 - Substitution for Visakha Bucha Day (May 11)
    Monday, June 2 - Special Government Holiday
    Tuesday, June 3 - H.M. the Queen's Birthday
    Thursday, July 10 - Asarnha Bucha Day
    Monday, July 28 - H.M. the King's Birthday
    Monday, August 11 - Special Government Holiday
    Tuesday, August 12 - H.M. the Queen Mother's Birthday / Mother's Day
    Monday, October 13 - H.M. King Bhumibol Memorial Day
    Thursday, October 23 - King Chulalongkorn Memorial Day
    Friday, December 5 - H.M. King Bhumibol's Birthday Anniversary / National Day / Father's Day
    Wednesday, December 10 - Constitution Day
    Wednesday, December 31 - New Year's Eve
    Floating Holidays:
    2 additional days for personal/religious observance
    Must be scheduled in advance with manager approval
    Holiday Pay Policy:
    Full-time employees receive 8 hours pay for each holiday
    Part-time employees receive pro-rated holiday pay
    Holiday falling on weekend observed on adjacent weekday
    Working Hours
    Standard Business Hours:
    Core Hours: 9:00 AM - 3:00 PM (all employees must be available)
    Flexible Start: Between 7:00 AM - 9:00 AM
    Flexible End: Between 3:00 PM - 6:00 PM
    Standard Workweek: 40 hours
    Remote Work Policy:
    Hybrid Schedule: Up to 2 days per week remote work
    Full Remote: Available for specific roles with approval
    Equipment: Company provides laptop and necessary software
    Home Office: $500 annual allowance for home office setup
    Overtime Policy:
    Non-Exempt Employees: Time and a half for hours over 40/week
    Exempt Employees: No overtime compensation
    Approval Required: All overtime must be pre-approved by manager
    CTEBA (Confidentiality, Trade Secrets, Ethics, Business Affairs)
    Confidentiality Agreement
    Proprietary Information: All company data, processes, and client information
    Non-Disclosure: Extends beyond employment termination
    Social Media: Prohibited from sharing confidential information
    Third Parties: Cannot disclose information to competitors or vendors
    Trade Secrets Protection
    Definition: Technical data, customer lists, pricing strategies, business plans
    Access Control: Information shared on need-to-know basis
    Document Security: Proper handling and storage of sensitive documents
    Digital Security: Strong passwords, secure file sharing, VPN usage required
    Ethics Guidelines
    Conflict of Interest: Must disclose any potential conflicts
    Gift Policy: No gifts over $50 from vendors or clients
    Fair Dealing: Honest and ethical treatment of customers, suppliers, competitors
    Harassment: Zero tolerance for harassment or discrimination
    Business Affairs Conduct
    Professional Representation: Employees represent company brand
    Client Relations: Maintain professional relationships at all times
    Vendor Relations: Fair and transparent dealings with all suppliers
    Intellectual Property: Respect copyrights, trademarks, and patents
    COMPANY FAQ
    General Information
    Q: What are the company's core values? A: Innovation, Integrity, Collaboration, Excellence, and
    Customer Focus.
    Q: How do I update my emergency contact information? A: Log into the HR portal and update your
    personal information, or contact HR directly.
    Q: Can I refer someone for employment? A: Yes! We offer a $1,000 referral bonus for successful
    hires who stay 90+ days.

    Benefits Questions
    Q: When am I eligible for benefits? A: Full-time employees are eligible after 30 days of employment.
    Q: How do I enroll in benefits? A: Complete enrollment through the HR portal during your first 30
    days or during open enrollment.
    Q: What happens to my benefits if I go on leave? A: Benefits continue during approved paid leave.
    Contact HR for unpaid leave scenarios.

    Time Off Questions
    Q: How do I request time off? A: Submit requests through the HR portal with at least 2 weeks notice
    for planned time off.

    Q: Can I donate PTO to a colleague? A: Yes, through our PTO donation program for employees facing
    medical emergencies.
    Q: What if I need emergency time off? A: Contact your manager immediately. Requests can be
    submitted retroactively for true emergencies.

    IT and Equipment
    Q: How do I get IT support? A: Submit tickets through the IT portal or call the help desk at ext. 4357.
    Q: Can I install software on my work computer? A: Only pre-approved software. Submit requests
    through IT for new software needs.
    Q: What's the policy on personal use of company equipment? A: Limited personal use is
    acceptable, but all activity is subject to monitoring.

    Performance and Development
    Q: How often are performance reviews conducted? A: Annual formal reviews in January, with midyear check-ins in July.
    Q: How do I request training or professional development? A: Discuss with your manager and
    submit requests through the learning portal.
    Q: Is there tuition reimbursement? A: Yes, up to $5,000/year for job-related education with preapproval.

    Contact Information
    HR Department: hr@techcorp.com | Ext. 5555
    IT Help Desk: it-support@techcorp.com | Ext. 4357
    Facilities: facilities@techcorp.com | Ext. 6666
    Employee Relations: employee-relations@techcorp.com | Ext. 5556"""

    return fqa



# Example usage:
if __name__ == "__main__":
    # Basic extraction
    # pdf_text = get_policy()
    pdf_text = get_FAQ()
    
    if pdf_text:
        print("Extracted text:")
        print(pdf_text[:500])  # Print first 500 characters
        print(f"\nTotal characters: {len(pdf_text)}")
    else:
        print("No text extracted or file not found")

