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
    def update_book(self, field, new):
        options = ["isbn", "title", "author", "publisher", "pub_year", "genre", "available", "total"]
        numeric_options = ["pub_year", "available", "total", "isbn"]
        
        field = field.strip().lower()

        if field not in options:
            return "Field not in valid options, valid fields:\n", options
        
        if field in numeric_options and type(new) != int:
            return f"'{field}' is a numeric field, and update type given is non-numeric '{new}' "
        
        # Validate all numeric options:
        
        current_value = getattr(self, field)

        setattr(self, field, new)
        return f"{current_value} was updated to {new}"
    
    def is_available(self):
        return self.available > 0
    
    def borrow_copy(self):
        if self.available > 0:
            self.available -= 1
            return True
        return False

    def return_copy(self):
        if self.available < self.total:
            self.available += 1

    # Displaying the object in desired and formatted way
    def __str__(self):
        # Formatting for courses and minors to be on new lines with dashes
        return (f"ISBN: {self.isbn}\n"
                f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Publisher: {self.publisher}\n"
                f"Published Year: {self.pub_year}\n"
                f"Genre: {self.genre}\n"
                f"Available: {self.available}\n"
                f"Total: {self.total}\n"
                f"---------------------------------------------------------------------------")

    # Useful for debugging
    # def __repr__(self):
    #     return (f"Student(student_id={self.get_student_id()}, "
    #             f"name={self.get_name()}, age={self.get_age()}, "
    #             f"courses={self.get_courses()}, minors={self.get_minor()})")    
            
# test = Book(None, None, None, None, None, None, 10, 12)
# print(test.update_book(0, "available", "s"))
# print(test.available)