def calculate_tax(salary):
    if salary <= 30000:
        return salary * 0.05
    elif salary <= 70000:
        return salary * 0.10
    else:
        return salary * 0.20