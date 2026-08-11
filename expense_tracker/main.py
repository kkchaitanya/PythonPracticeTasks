from tracker.file_handler import load_all, save_all
from tracker.expenses import add_expenses, display_all_expenses, remove_expense, search_expense, update_expense
from tracker.menu import get_choice, get_expense_input, get_search_keyword, get_update_input, show_menu


def main():
    # Initialize in-memory storage
    expenses = []
    # Load existing data
    try:
        expenses = load_all()
    except Exception as e:
        print("Warning: Could not load existing data.")

    # Main loop
    while True:
         show_menu()
         choice = get_choice()
         if choice == "1":  # Add expense
            data = get_expense_input()
            if data:
                add_expenses(expenses, *data)
         elif choice == "2":  # Remove expense
            expense_id = input("Enter expense ID to remove: ").strip()
            remove_expense(expenses, expense_id)
         elif choice == "3":  # Update expense
                data = get_update_input()
                if data:
                    expense_id, date, category, amount, description = data
                    update_expense(expenses, expense_id, date, category, amount, description)
         elif choice == "4":  # Search expense
                keyword = get_search_keyword()
                if keyword:
                    search_expense(expenses, keyword)
         elif choice == "5":  # Display All
                display_all_expenses(expenses)
         elif choice == "6":  # Save to File
            try:
                save_all(expenses)
                print("Data saved successfully to students.txt")
            except Exception as e:
                print(f"Failed to save: {e}")
         elif choice == "7":  # Exit
                try:
                    save_all(expenses)
                    print("Data saved. Goodbye!")
                    break
                except Exception as e:
                    print("Error during exit save. Exiting anyway.")
                    break
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"Unexpected fatal error: {e}")