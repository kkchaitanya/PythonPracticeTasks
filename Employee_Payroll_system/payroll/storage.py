import csv
import os

FILE_NAME = "employees.csv"


def save_employee(employee):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["emp_id", "name", "salary"]
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(employee)


def get_employee(emp_id):

    if not os.path.exists(FILE_NAME):
        return None

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["emp_id"] == emp_id:
                return row

    return None