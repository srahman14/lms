from models.book import Book
from library_operations import add_book, list_all_books
from storage import load_books, save_books
from models.catalog import Catalog

cat = Catalog()
# cat.add_book(isbn=1234567890, title="Harry Potter", author="J.K Rowling", publisher="Owl", pub_year=2005, genre="Sci-fi", available=15, total=20)
# cat.add_book(isbn=1234567891, title="Atomic Habits", author="James Clear", publisher="Fox", pub_year=2002, genre="Productivity", available=10, total=20)
# cat.add_book(isbn=1234567892, title="Test", author="Test Author", publisher="Test Pub", pub_year=2005, genre="Test Genre", available=10, total=20)
# list_all_books()

# cat.remove_book(isbn=1234567890)
# cat.remove_book(isbn=1234567891)
# cat.view_books()
# cat.update_book(1234567892, field="Author", new_val="Test Update Author")
# cat.check_availablity(1234567891)
# cat.search_books(isbn=None, title="Test", author="James Clear", genre=None)
