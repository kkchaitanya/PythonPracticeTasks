class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.borrowed = False

    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f"ID: {self.book_id} | {self.title} | {self.author} | {status}"