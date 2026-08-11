# main.py
from sms import (
    add_student, remove_student, update_student, search_student,
    display_all_students, save_students, load_students
)
from sms.menu import show_menu, get_choice, get_student_input, get_update_input, get_search_keyword, display_students
from sms.logger_setup import setup_logger


def main():
    # Setup logger
    logger = setup_logger("student.log")

    # Initialize in-memory storage
    students = []

    # Load existing data
    try:
        students = load_students("students.txt", logger)
    except Exception as e:
        logger.error(f"Startup load error: {e}")
        print("Warning: Could not load existing data.")

    # Main loop
    while True:
        show_menu()
        choice = get_choice()

        if choice is None:
            continue

        if choice == "1":  # Add Student
            data = get_student_input()
            if data:
                add_student(students, *data, logger=logger)

        elif choice == "2":  # Remove Student
            student_id = input("Enter Student ID to remove: ").strip()
            remove_student(students, student_id, logger=logger)

        elif choice == "3":  # Update Student
            data = get_update_input()
            if data:
                student_id, name, age, grade, email = data
                update_student(students, student_id, name, age, grade, email, logger=logger)

        elif choice == "4":  # Search Student
            keyword = get_search_keyword()
            if keyword:
                results = search_student(students, keyword, logger=logger)
                display_students(results, title=f"Search Results for '{keyword}'")

        elif choice == "5":  # Display All
            all_students = display_all_students(students, logger=logger)
            display_students(all_students, title="All Students")

        elif choice == "6":  # Save to File
            try:
                save_students(students, "students.txt", logger)
                print("Data saved successfully to students.txt")
            except Exception as e:
                print(f"Failed to save: {e}")

        elif choice == "7":  # Exit
            try:
                save_students(students, "students.txt", logger)
                logger.info("Application exited normally.")
                print("Data saved. Goodbye!")
                break
            except Exception as e:
                logger.error(f"Exit save error: {e}")
                print("Error during exit save. Exiting anyway.")
                break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"Unexpected fatal error: {e}")
