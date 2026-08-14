# customers.py

import csv
import os

CUSTOMER_FILE = "customers.csv"


def initialize_customer_file():
    """
    Create customer file with header if it doesn't exist.
    """
    if not os.path.exists(CUSTOMER_FILE):
        with open(CUSTOMER_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["account_no", "name", "balance"])


def read_customers():
    """
    Read all customers and return as a list.
    """
    initialize_customer_file()

    customers = []

    with open(CUSTOMER_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["balance"] = float(row["balance"])
            customers.append(row)

    return customers


def generate_account_number():
    """
    Generate next account number.
    """
    customers = read_customers()

    if not customers:
        return 1001

    last_account = int(customers[-1]["account_no"])

    return last_account + 1


def create_account(name, initial_balance,logger=None):
    try:
        """
        Create a new bank account.
        """
        account_no = generate_account_number()

        with open(CUSTOMER_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([account_no, name, initial_balance])

        logger.info(f"Account Created | Account:{account_no}")

        return account_no
    except Exception as ex:
        logger.error(f"create_account exception:{ex}")


def get_customer(account_no):
    """
    Return customer details by account number.
    """
    customers = read_customers()

    for customer in customers:
        if customer["account_no"] == str(account_no):
            return customer

    return None


def check_balance(account_no):
    """
    Return account balance.
    """
    customer = get_customer(account_no)

    if customer:
        return customer["balance"]

    return None


def update_balance(account_no, new_balance,logger=None):
    """
    Update customer balance.
    """
    customers = read_customers()

    for customer in customers:
        if customer["account_no"] == str(account_no):
            customer["balance"] = new_balance
            break

    with open(CUSTOMER_FILE, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["account_no", "name", "balance"])

        for customer in customers:
            writer.writerow(
                [
                    customer["account_no"],
                    customer["name"],
                    customer["balance"]
                ]
            )

    logger.info(
        f"Balance Updated | Account:{account_no} | New Balance:{new_balance}"
    )


def get_all_customers():
    """
    Return all customer records.
    """
    return read_customers()


# acc1 = create_account("Krishna", 5000)
# acc2 = create_account("Ram", 3000)
# print(get_customer(acc1))
# print(check_balance(acc1))
# update_balance(acc1, 7000)
# print(check_balance(acc1))
# print(get_all_customers())