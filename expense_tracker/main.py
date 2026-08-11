from tracker.logger import setup_logger
from tracker.file_handler import load_all, save_all
from tracker.expenses import add_expenses, display_all_expenses, remove_expense, search_expense, update_expense
from tracker.menu import get_choice, get_expense_input, get_search_keyword, get_update_input, show_menu


def main():
     # Setup logger
    logger = setup_logger("logs/expense.log")
    # Initialize in-memory storage
    expenses = []
    # Load existing data
    try:
        expenses = load_all(logger)
    except Exception as e:
        print("Warning: Could not load existing data.")
        logger.error(f"Warning: Could not load existing data.{e}")

    # Main loop
    while True:
         show_menu()
         choice = get_choice()
         if choice == "1":  # Add expense
            data = get_expense_input()
            if data:
                add_expenses(expenses, *data,logger)
         elif choice == "2":  # Remove expense
            expense_id = input("Enter expense ID to remove: ").strip()
            remove_expense(expenses, expense_id,logger)
         elif choice == "3":  # Update expense
                data = get_update_input()
                if data:
                    expense_id, date, category, amount, description = data
                    update_expense(expenses, expense_id, date, category, amount, description,logger)
         elif choice == "4":  # Search expense
                keyword = get_search_keyword()
                if keyword:
                    search_expense(expenses, keyword)
         elif choice == "5":  # Display All
                display_all_expenses(expenses)
         elif choice == "6":  # Save to File
            try:
                save_all(expenses,logger)
                print("Data saved successfully to expenses.csv")
                logger.info("Data saved successfully to expenses.csv")
            except Exception as e:
                print(f"Failed to save: {e}")
                logger.error(f"Failed to save:.{e}")
         elif choice == "7":  # Exit
                try:
                    save_all(expenses,logger)
                    print("Data saved. Goodbye!")
                    logger.info("Data saved. Goodbye!")
                    break
                except Exception as e:
                    print("Error during exit save. Exiting anyway.")
                    logger.error(f"Error during exit save. Exiting anyway.{e}")
                    break
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"Unexpected fatal error: {e}")