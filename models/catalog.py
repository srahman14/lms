# The Catalog is the central manager for all books in the system. 
# responsible for storing, organizing, searching, and manipulating book entries.

# Key Responsibilities of the Catalog:
# Managing the collection of books — loading and saving books.
# Searching for books by title, author, genre, or ISBN.
# Adding new books and checking for duplicates.
# Removing books by ISBN.
# Updating existing books.
# Handling availability — checking if a book is available, how many copies remain, etc.
# Optionally: Filtering or sorting books by year, genre, etc.

from models.book import Book
from storage import load_books, save_books
from validation import validate_isbn

class Catalog:
    def __init__(self):
        self.books = load_books()

    def add_book(self, isbn: int, title: str, author: str, publisher: str, pub_year: int, genre: str, available: int, total: int):
        try:
            # Validate the ISBN is unique
            validate_isbn(isbn)
            # Load students from students.json
            books_data = load_books()
            # If student is an undergrad, then use undergraduate class, else Student class
            new_book = Book(isbn, title, author, publisher, pub_year, genre, available, total)
            # Add the new student to the existing student database
            books_data.append(new_book)

            # Save the new students by passing the new list of students as a parameter
            save_books(books_data)
            print(f"Book with ISBN: {isbn} has been added successfully!")

        except Exception as e:
            print(f"Unexpected error: {e}")
    
