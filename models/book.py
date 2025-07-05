
class Book:
    def __init__(self, isbn, title, author, publisher, pub_year, genre, available, total):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pub_year = pub_year
        self.genre = genre
        # Number of Books Available to Loan out
        self.available = available
        # Number of Copies in total
        self.total = total

    # Update Book Details
    def update_book(self, isbn, field, new):
        options = ["isbn", "title", "author", "publisher", "pub_year", "genre", "available", "total"]
        numeric_options = ["pub_year", "available", "total", "isbn"]
        # Verify ISBN is valid (for now just going to skip this as no database)

        if field not in options:
            return "Field not in valid options"
        
        if field in numeric_options and type(new) != int:
            return f"'{field}' is a numeric field, and update type given is non-numeric '{new}' "
        
        # Validate all numeric options:
        
        current_value = getattr(self, field)

        setattr(self, field, new)
        return f"{current_value} was updated to {new}"
    

            
test = Book(None, None, None, None, None, None, 10, 12)
print(test.update_book(0, "available", "s"))
print(test.available)