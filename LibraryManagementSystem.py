# ============================================
#   LIBRARY MANAGEMENT SYSTEM
# ============================================

# Dictionary to store books
library = {}

# Welcome message
print("=" * 55)
print("    WELCOME TO LIBRARY MANAGEMENT SYSTEMs")
print("=" * 55)

# Main program loop
while True:
    print("\n" + "=" * 55)
    print("         MAIN MENU")
    print("=" * 55)
    print("  1.  Add Book")
    print("  2.  Borrow Book")
    print("  3.  Return Book")
    print("  4.  Search Book")
    print("  5.  Display Books")
    print("  6.  Exit")
    print("=" * 55)

    choice = input("Enter your choice (1-6): ").strip()

    # ---------- ADD BOOK ----------
    if choice == "1":
        print("\n ADD A NEW BOOK")
        print("-" * 40)

        title = input("Enter book title: ").strip().lower()
        author = input("Enter author name: ").strip()

        if not title or not author:
            print(" Title and Author cannot be empty.")
        elif title in library:
            print(f" '{library[title]['title']}' already exists in the library.")
        else:
            library[title] = {
                "title": title.title(),
                "author": author.title(),
                "available": True,
                "borrower": None
            }
            print(f" Book '{title.title()}' added successfully!")

    # ---------- BORROW BOOK ----------
    elif choice == "2":
        print("\n BORROW A BOOK")
        print("-" * 40)

        title = input("Enter book title to borrow: ").strip().lower()

        if title not in library:
            print(f" Book '{title}' not found in the library.")
        elif not library[title]["available"]:
            print(f" '{library[title]['title']}' is already borrowed by {library[title]['borrower']}.")
        else:
            borrower = input("Enter borrower name: ").strip()
            if not borrower:
                print(" Borrower name cannot be empty.")
            else:
                library[title]["available"] = False
                library[title]["borrower"] = borrower.title()
                print(f" '{library[title]['title']}' borrowed successfully by {borrower.title()}.")

    # ---------- RETURN BOOK ----------
    elif choice == "3":
        print("\n RETURN A BOOK")
        print("-" * 40)

        title = input("Enter book title to return: ").strip().lower()

        if title not in library:
            print(f" Book '{title}' does not belong to this library.")
        elif library[title]["available"]:
            print(f" '{library[title]['title']}' was not borrowed. Cannot return an available book.")
        else:
            print(f" '{library[title]['title']}' returned successfully by {library[title]['borrower']}.")
            library[title]["available"] = True
            library[title]["borrower"] = None

    # ---------- SEARCH BOOK ----------
    elif choice == "4":
        print("\n SEARCH FOR A BOOK")
        print("-" * 40)

        keyword = input("Enter title or author to search: ").strip().lower()
        if not keyword:
            print(" Search keyword cannot be empty.")
        else:
            results = []
            for book in library.values():
                if keyword in book["title"].lower() or keyword in book["author"].lower():
                    results.append(book)

            if not results:
                print(f" No books found matching '{keyword}'.")
            else:
                print(f"\n📋 Found {len(results)} result(s):")
                print("-" * 60)
                print(f"{'Title':<25}{'Author':<20}{'Status':<15}")
                print("-" * 60)
                for book in results:
                    if book["available"]:
                        status = "Available ✅"
                    else:
                        status = f"Borrowed by {book['borrower']} "
                    print(f"{book['title']:<25}{book['author']:<20}{status:<15}")

    # ---------- DISPLAY BOOKS ----------
    elif choice == "5":
        print("\n LIBRARY CATALOG")
        print("=" * 70)

        if not library:
            print(" Library is empty. Add some books first.")
        else:
            # Separate available and borrowed books
            available_books = []
            borrowed_books = []
            for book in library.values():
                if book["available"]:
                    available_books.append(book)
                else:
                    borrowed_books.append(book)

            # Available books
            print(f"\n AVAILABLE BOOKS ({len(available_books)}):")
            print("-" * 70)
            if available_books:
                print(f"{'Title':<25}{'Author':<20}{'Status':<15}")
                print("-" * 70)
                for book in available_books:
                    print(f"{book['title']:<25}{book['author']:<20}{'Available':<15}")
            else:
                print("   No books currently available.")

            # Borrowed books
            print(f"\n BORROWED BOOKS ({len(borrowed_books)}):")
            print("-" * 70)
            if borrowed_books:
                print(f"{'Title':<25}{'Author':<20}{'Borrower':<20}")
                print("-" * 70)
                for book in borrowed_books:
                    print(f"{book['title']:<25}{book['author']:<20}{book['borrower']:<20}")
            else:
                print("   No books currently borrowed.")

            # Statistics
            print("\n" + "=" * 70)
            print(f" Total Books in Library : {len(library)}")
            print(f" Available Books        : {len(available_books)}")
            print(f" Borrowed Books         : {len(borrowed_books)}")
            print("=" * 70)

    # ---------- EXIT ----------
    elif choice == "6":
        print("\n Thank you for using the Library Management System!")
        print("📖 Happy Reading! See you again!\n")
        break

    # ---------- INVALID CHOICE ----------
    else:
        print(" Invalid choice. Please enter a number between 1 and 6.")
