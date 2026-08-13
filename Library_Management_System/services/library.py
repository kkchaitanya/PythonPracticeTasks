from models.book import Book
from exceptions.custom_exceptions import *
import logging

logging.basicConfig(
    filename="logs/library.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author):

        if not isinstance(book_id, int):
            raise InvalidBookIDException("Book ID must be numeric.")

        book = Book(book_id, title, author)
        self.books.append(book)

        print("Book added successfully!")

    def search_book(self, book_id):

        if not isinstance(book_id, int):
            raise InvalidBookIDException("Invalid Book ID.")

        for book in self.books:
            if book.book_id == book_id:
                return book

        raise BookNotFoundException("Book not found.")

    def borrow_book(self, book_id):

        book = self.search_book(book_id)

        if book.borrowed:
            raise AlreadyBorrowedException(
                "Book already borrowed."
            )

        book.borrowed = True

        logging.info(f"BORROWED -> {book.title}")

        with open("history.txt", "a") as file:
            file.write(f"Borrowed: {book.title}\n")

        print("Book borrowed successfully!")

    def return_book(self, book_id):

        book = self.search_book(book_id)

        if not book.borrowed:
            print("Book was not borrowed.")
            return

        book.borrowed = False

        logging.info(f"RETURNED -> {book.title}")

        with open("history.txt", "a") as file:
            file.write(f"Returned: {book.title}\n")

        print("Book returned successfully!")

    def view_available_books(self):

        print("\nAvailable Books:\n")

        found = False

        for book in self.books:
            if not book.borrowed:
                print(book)
                found = True

        if not found:
            print("No books available.")

    def view_history(self):

        try:
            with open("history.txt", "r") as file:
                print("\nBorrow History:")
                print(file.read())

        except FileNotFoundError:
            print("No history available.")