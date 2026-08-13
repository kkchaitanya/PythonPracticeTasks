from payroll.employee import add_employee
from payroll.storage import save_employee, get_employee
from payroll.salary import calculate_net_salary
from payroll.payslip import generate_payslip
from payroll.exceptions import (
    InvalidSalaryError,
    EmployeeNotFoundError,
    InvalidInputError,
    EmployeeAlreadyExists
)
from payroll.logger import payroll_logger, error_logger


def add_employee_record():

    try:
        emp_id = input("Enter Employee ID: ").strip()
        name = input("Enter Employee Name: ").strip()

        salary = float(input("Enter Salary: "))

        if salary <= 0:
            raise InvalidSalaryError("Salary must be greater than zero.")
       
        employee = add_employee(emp_id, name, salary)
        already_existing= get_employee(emp_id)
        if already_existing==None:
            save_employee(employee)
            print("Employee added successfully.")
        else :
             raise EmployeeAlreadyExists(f"Emplyee with Employee Id  {emp_id} already exists")
        

    except InvalidSalaryError as e:
        print(e)
        error_logger.error(e)

    except ValueError:
        error_logger.error("Invalid salary entered.")
        print("Salary must be numeric.")

    except Exception as e:
        error_logger.error(e)
        print(e)


def generate_employee_payslip():

    try:
        emp_id = input("Enter Employee ID: ").strip()

        if not emp_id:
            raise InvalidInputError("Employee ID cannot be empty.")

        employee = get_employee(emp_id)

        if employee is None:
            raise EmployeeNotFoundError("Employee not found.")

        salary = float(employee["salary"])

        salary_details = calculate_net_salary(salary)

        payroll_logger.info(
            f"Salary generated for Employee ID {emp_id}"
        )

        payslip = generate_payslip(
            employee,
            salary_details
        )

        print(payslip)

    except EmployeeNotFoundError as e:
        print(e)
        error_logger.error(e)

    except InvalidInputError as e:
        print(e)
        error_logger.error(e)

    except Exception as e:
        print(e)
        error_logger.error(e)


def menu():

    while True:

        print("\n===== EMPLOYEE PAYROLL SYSTEM =====")
        print("1. Add Employee")
        print("2. Generate Payslip")
        print("3. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_employee_record()

        elif choice == "2":
            generate_employee_payslip()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            error_logger.error("Invalid menu choice.")
            print("Invalid Choice")


menu()