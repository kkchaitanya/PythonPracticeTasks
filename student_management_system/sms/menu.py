# sms/menu.py
from .manager import format_student

def show_menu():
    """Displays the main menu options."""
    print("\n" + "=" * 50)
    print("        STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display All Students")
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


def get_student_input():
    """Collects student data from user."""
    try:
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Name: ").strip()
        age = input("Enter Age: ").strip()
        grade = input("Enter Grade: ").strip()
        email = input("Enter Email: ").strip()
        return student_id, name, age, grade, email
    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled.")
        return None


def get_update_input():
    """Collects optional update fields from user."""
    try:
        student_id = input("Enter Student ID to update: ").strip()
        name = input("Enter new Name (or press Enter to skip): ").strip() or None
        age_input = input("Enter new Age (or press Enter to skip): ").strip()
        age = int(age_input) if age_input else None
        grade = input("Enter new Grade (or press Enter to skip): ").strip() or None
        email = input("Enter new Email (or press Enter to skip): ").strip() or None
        return student_id, name, age, grade, email
    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled.")
        return None
    except ValueError:
        print("Error: Age must be an integer.")
        return None


def get_search_keyword():
    """Gets search keyword from user."""
    try:
        return input("Enter search keyword (ID/Name/Email): ").strip()
    except (KeyboardInterrupt, EOFError):
        return None


def display_students(students, title="Students"):
    """Pretty-prints a list of students."""
    if not students:
        print(f"\n{title}: No records found.")
        return
    print(f"\n--- {title} ({len(students)} record(s)) ---")
    print("-" * 50)
    for i, s in enumerate(students, 1):
        print(f"{i}. {format_student(s)}")
    print("-" * 50)
