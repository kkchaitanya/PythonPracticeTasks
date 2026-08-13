from payroll.tax import calculate_tax
from payroll.bonus import calculate_bonus


def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    bonus = calculate_bonus(salary)

    net_salary = salary + bonus - tax

    return {
        "basic_salary": salary,
        "bonus": bonus,
        "tax": tax,
        "net_salary": net_salary
    }