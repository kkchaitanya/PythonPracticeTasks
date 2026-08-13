from services.library import Library
from exceptions.custom_exceptions import *

library = Library()


def display_menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View Available Books")
    print("6. View Borrowing History")
    print("7. Exit")


while True:

    display_menu()

    choice = input("Enter your choice: ")

    try:

        if choice == "1":

            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")

            library.add_book(book_id, title, author)

        elif choice == "2":

            book_id = int(input("Enter Book ID: "))
            library.borrow_book(book_id)

        elif choice == "3":

            book_id = int(input("Enter Book ID: "))
            library.return_book(book_id)

        elif choice == "4":

            book_id = int(input("Enter Book ID: "))
            book = library.search_book(book_id)

            print("\nBook Found:")
            print(book)

        elif choice == "5":

            library.view_available_books()

        elif choice == "6":

            library.view_history()

        elif choice == "7":

            print("Thank you!")
            break

        else:
            print("Invalid Choice!")

    except BookNotFoundException as e:
        print("Error:", e)

    except AlreadyBorrowedException as e:
        print("Error:", e)

    except InvalidBookIDException as e:
        print("Error:", e)

    except ValueError:
        print("Error: Enter numeric value for Book ID.")

    except Exception as e:
        print("Unexpected Error:", e)