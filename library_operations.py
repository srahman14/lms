from models.book import Book
from storage import load_books, save_books

def add_book(isbn: int, title: str, author: str, publisher: str, pub_year: int, genre: str, available: int, total: int):
        try:
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


# Function for listing all students in the books database (cRud - Read)
def list_all_books():
    # Load the bookss
    book_data = load_books()
    for i in book_data:
        # This uses the __str__ format for displaying books objects, defined in the books class
        print(i)