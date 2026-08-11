import csv
import os
from dateutil.parser import parse
FILE = "data/expenses.csv"
FIELDNAMES = ["id", "date", "category", "amount", "description"]

def save_all(expenses):
    """Write the entire list back to CSV (used for update/delete)."""
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)

def load_all():
    """Read CSV and return list of dicts. Convert types."""
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        expenses = []
        for row in reader:
            row["id"] = int(row["id"])
            row["date"] = parse(row["date"]).date()
            row["category"] = int(row["category"])
            row["amount"] = float(row["amount"])
            row["description"] = str(row["description"])
            expenses.append(row)
        return expenses

def append_one(expense):
    """Add a single new expense to the end."""
    file_exists = os.path.exists(FILE)
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if not file_exists:
            writer.writeheader()
        writer.writerow(expense)
