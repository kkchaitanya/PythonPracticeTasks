
import datetime
from dateutil.parser import parse

def validate_inputs(expense_id, date, category, amount, description,logger=None):
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
    except (TypeError, ValueError) as ex:
            logger.error(f"Failed to load file: {ex}")
            raise ValueError("amount must be a valid float.")
        
    
def get_expense_by_id(expenses, expense_id):
    """Returns a student dictionary by ID, or None."""
    for s in expenses:
        if s["id"] == int(expense_id):
            return s
    return None

def add_expenses(expenses, expense_id, date, category, amount, description,logger=None):
    """ add new expenses to the CSV file"""
    try: 
         ## validate input ##
         validate_inputs(expense_id, date, category, amount, description)
         if get_expense_by_id(expenses, expense_id):
            logger.error(f"expense ID {expense_id} already exists.")
            raise ValueError(f"expense ID {expense_id} already exists.")
         expenses.append({
                    "id": str(expense_id).strip(),
                    "date":  parse(date).date(),
                    "category": str(category).strip(),
                    "amount": float(amount),
                    "description": str(description).strip()
                })
         logger.info(f"add_expenses completed")
    except Exception as ex:
        print(f"Error: {ex}")
        logger.error(f"Failed to load file: {ex}")
        return False
    
def remove_expense(expenses, expense_id,logger=None):
    """Removes a expense by ID."""
    try:
        expense = get_expense_by_id(expenses, expense_id)
        if not expense_id:
            raise ValueError(f"Student ID {expense_id} not found.")
        expense.remove(expense)
        logger.info(f"remove_expense completed")
        return True
    except ValueError as ve:
        print(f"Error: {ve}")
        logger.error(f"Failed to load file: {ve}")
        return False
    
def update_expense(expenses, expense_id, date=None, category=None, amount=None, description=None,logger=None):
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
        logger.info(f"update_expense completed")
        return True
    except Exception as ex:
        print(f"Error: {ex}")
        logger.error(f"Failed to load file: {ex}")
        return False
    
def search_expense(expenses, keyword,logger):
    """Searches search_expense by ID, deascription."""
    try:
        keyword = str(keyword).lower()
        results = [
            item for item in expenses
            if any(
            keyword.lower() in str(item.get(col, "")).lower()
            for col in ["date", "category", "description"]
            )
            ]
        display_expenses(results)
        logger.info(f"search_expense completed")
        return results
    except Exception as e:
        logger.error(f"Failed to load file: {e}")
        return []

def display_all_expenses(expenses):
    """Returns the list of all expenses (for display)."""
    display_expenses(expenses)
    return expenses

def display_expenses(expenses):
    print(f"{'ID':<5} {'DATE':<12} {'CATEGORY':<15} {'AMOUNT':<10} {'DESCRIPTION'}")
    for item in expenses:
        print(
            f"{item['id']:<5} "
            f"{str(item['date']):<12} "
            f"{item['category']:<15} "
            f"{item['amount']:<10} "
            f"{item['description']}"
        )