
def show_menu():
    """Displays the main menu options."""
    print("\n" + "=" * 50)
    print("        Expense Tracker SYSTEM")
    print("=" * 50)
    print("1. Add Expense")
    print("2. Remove Expense")
    print("3. Update Expense")
    print("4. Search Expense")
    print("5. Display All Expense")
    print("6. Save Data to File")
    print("7. Exit")
    print("=" * 50)

def get_choice():
    """Gets and validates the menu choice."""
    try:
        choice = input("Enter your choice (1-7): ").strip()
        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            raise ValueError("Choice must be between 1 and 7.")
        return choice
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    
def get_expense_input():
    """Collects expense data from user."""
    try:
        expense_id = input("Enter expense ID: ").strip()
        date = input("Enter a date (YYYY-MM-DD):").strip()
        category = input("Enter category: ").strip()
        amount = input("Enter amount: ").strip()
        description = input("Enter description: ").strip()
        return expense_id, date, category, amount, description
    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled.")
        return None
    
def get_update_input():
    """Collects optional update fields from user."""
    try:
        expense_id = input("Enter expense ID to update: ").strip()
        date = input("Enter date (or press Enter to skip): ").strip() or None
        category = input("Enter category (or press Enter to skip): ").strip()
        amount = input("Enter amount (or press Enter to skip): ").strip() or None
        description = input("Enter description (or press Enter to skip): ").strip() or None
        return expense_id, date, category, amount, description
    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled.")
        return None
    except ValueError:
        print("Error: Age must be an integer.")
        return None

def get_search_keyword():
    """Gets search keyword from user."""
    try:
        return input("Enter search keyword (ID/category/description): ").strip()
    except (KeyboardInterrupt, EOFError):
        return None