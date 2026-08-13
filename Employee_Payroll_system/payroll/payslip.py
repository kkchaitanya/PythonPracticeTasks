def generate_payslip(employee, salary_details):

    payslip = f"""
=============================
         PAYSLIP
=============================
Employee ID : {employee['emp_id']}
Employee Name : {employee['name']}

Basic Salary : {salary_details['basic_salary']}
Bonus        : {salary_details['bonus']}
Tax          : {salary_details['tax']}
Net Salary   : {salary_details['net_salary']}
=============================
"""

    return payslip