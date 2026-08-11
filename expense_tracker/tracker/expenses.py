
import datetime
from dateutil.parser import parse

def validate_inputs(expense_id, date, category, amount, description):
    """Validates all expense input fields """
    if not expense_id or not str(expense_id).strip():
        raise ValueError("Expense ID cannot be empty.")
    if not date or not str(date).strip():
        raise ValueError("Date cannot be empty.")
    if not category or not str(category).strip():
        raise ValueError("Category cannot be empty.")
    if not amount or not str(amount).strip():
        raise ValueError("Amount cannot be empty.")
    if not description or not str(description).strip():
        raise ValueError("Description cannot be empty.")
    try:
            age_int = float(amount)
    except (TypeError, ValueError):
            raise ValueError("amount must be a valid float.")
    
def get_expense_by_id(expenses, expense_id):
    """Returns a student dictionary by ID, or None."""
    for s in expenses:
        if s["id"] == expense_id:
            return s
    return None

def add_expenses(expenses, expense_id, date, category, amount, description):
    """ add new expenses to the CSV file"""
    try: 
         ## validate input ##
         validate_inputs(expense_id, date, category, amount, description)
         if get_expense_by_id(expenses, expense_id):
            raise ValueError(f"expense ID {expense_id} already exists.")
         expenses.append({
                    "id": str(expense_id).strip(),
                    "date":  parse(date).date(),
                    "category": str(category).strip(),
                    "amount": float(amount),
                    "description": str(description).strip()
                })
    except Exception as ex:
        print(f"Error: {ex}")
        return False
    
def remove_expense(expenses, expense_id):
    """Removes a expense by ID."""
    try:
        expense = get_expense_by_id(expenses, expense_id)
        if not expense_id:
            raise ValueError(f"Student ID {expense_id} not found.")
        expense.remove(expense)
        return True
    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    
def update_expense(expenses, expense_id, date=None, category=None, amount=None, description=None):
    """Updates fields of an existing student."""
    try:
        expense = get_expense_by_id(expenses, expense_id)
        if not expense:
            raise ValueError(f"expense ID {expense_id} not found.")
        if date is not None:
            expense["date"] = (parse(date).date())
        if category is not None:
            expense["category"] = str(category).strip()
        if amount is not None:
            expense["amount"] = float(amount)
        if description is not None:
            expense["description"] = str(description)   
        return True
    except Exception as ex:
        print(f"Error: {ex}")
        return False
    
def search_expense(expenses, keyword):
    """Searches students by ID, name, or email."""
    try:
        keyword = str(keyword).lower()
        results = [
            s for s in expenses
            if keyword in s["id"].lower()
            or keyword in s["category"].lower()
            or keyword in s["description"].lower()
        ]
        return results
    except Exception as e:
        return []

def display_all_expenses(expenses):
    """Returns the list of all expenses (for display)."""
    return expenses