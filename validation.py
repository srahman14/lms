import re

# Validation for following fields
# ["isbn", "title", "author", "publisher", "pub_year", "genre", "available", "total"]

# validate ISBN 
# Must be unique (no duplicate books with same ISBN).
# Must be a positive integer (or alternatively, a string of 10 or 13 digits depending on ISBN format).
# Must not contain letters, special characters, or spaces.
# Must be present (required field).

def validate_isbn(isbn: int):
    # Must be Unique
    # Would have to check database

    str_isbn = str(isbn)
    # Validate ISBN not empty
    if len(str_isbn) == 0: return "ISBN cannot be an empty field" 
    # Validate Length (10-13 digits min)
    if len(str_isbn) != 10 or len(str_isbn) != 13:
        return f"Invalid ISBN - ISBN must be 10 or 13 digits, '{str_isbn}' digits was given"
    
    # Validate if any letters or special chars or spaces present
    if str_isbn.strip() != str_isbn:
        return "There must be no spaces presenst in the ISBN"
    
    str_isbn_list = [i for i in str_isbn if i.isdigit == False]
    if str_isbn_list > 0: return f"ISBN must not contain any letters, {str_isbn_list} letters/characters were present"



# ["isbn", "title", "author", "publisher", "pub_year", "genre", "available", "total"]


# validate TITLE
# Must be a non-empty string.
# Max length: 255 characters.
# Should not contain only whitespace.
# Can contain letters, numbers, and common punctuation (like colons or dashes).

# Must be a non-empty string.
# Max length: 100–150 characters.
# Should contain only letters, spaces, and optional periods (e.g., "J.K. Rowling").
# Should not include numbers or symbols.

def valdiate_str(title: None, author: None, publisher: None, genre: None):
    if title is None and author is None and publisher is None and genre is None: return "No input to validate"

    numbers = list(range(0,10))
    symbols = "!@£$%^&**()_-+=[]:'/?,<>}{`'"
    
    if title: 
        if type(title) != str: return "Invalid Title, Title must be a string"
        if len(title.strip()) == 0: return "Invalid Title, empty title was given"
        if len(title) > 255: return "Invalid Title \n Max length: 255 chars"

    if author:
        if type(author) != str: return "Invalid entry for author\n Error: entry must be a string"
        if len(author.strip()) == 0: return "Invalid entry for author\n Error: empty entry was given"
        if len(author) > 100: return "Invalid entry for author\n Error: Max length: 100 chars"

        num_errors = []
        sym_errors = []

        for i in author:
            if i in numbers:
                num_errors.append(i)
            if i in symbols: 
                sym_errors.append(i)

        if num_errors and sym_errors:
            return f"Invalid entry for author \n Error: Cannot contain any numbers or symbols\n Numbers Present: '{"".join(num_errors)}'\n Symbols present: '{"".join(sym_errors)}'"
        
        if num_errors:
            return f"Invalid entry for author \n Error: Cannot contain any numbers or symbols\n Numbers Present: '{"".join(num_errors)}'\n'"

        if sym_errors:
            return f"Invalid entry for author \n Error: Cannot contain any symbols\n Symbolds Present: '{"".join(sym_errors)}'\n'"

    if publisher:
        if type(publisher) != str: return "Invalid entry for publisher\n Error: entry must be a string"
        if len(publisher.strip()) == 0: return "Invalid entry for publisher\n Error: empty entry was given"
        if len(publisher) > 150: return "Invalid entry for publisher\n Error: Max length: 100 chars"

        num_errors = []
        sym_errors = []

        for i in publisher:
            if i in numbers:
                num_errors.append(i)
            if i in symbols: 
                sym_errors.append(i)

        if num_errors and sym_errors:
            return f"Invalid entry for publisher \n Error: Cannot contain any numbers or symbols\n Numbers Present: '{"".join(num_errors)}'\n Symbols present: '{"".join(sym_errors)}'"
        
        if num_errors:
            return f"Invalid entry for publisher \n Error: Cannot contain any numbers or symbols\n Numbers Present: '{"".join(num_errors)}'\n'"

        if sym_errors:
            return f"Invalid entry for publisher \n Error: Cannot contain any symbols\n Symbolds Present: '{"".join(sym_errors)}'\n'"

              
# 4. Publisher
# Must be a non-empty string.
# Max length: 150 characters.
# Can include letters, numbers, and standard publishing terms (e.g., "Inc.", "Ltd.").
# Should not be just whitespace or special characters.

# 5. Publication Year (pub_year)
# Must be an integer.

# Must be greater than 1440 (the invention of the printing press).

# Must be less than or equal to the current year.

# Should reject future years.

# 6. Genre
# Must be a non-empty string.

# Max length: 50 characters.

# Should match a predefined list of genres (optional, for consistency — e.g., “Fiction”, “Biography”, etc.).

# No numbers or symbols unless part of a real genre (e.g., "Sci-Fi").

# 7. Available Copies (available)
# Must be an integer.

# Must be ≥ 0.

# Cannot be greater than total copies.

# Should default to total when book is first added unless specified otherwise.

# 8. Total Copies (total)
# Must be an integer.

# Must be ≥ 1 (a book cannot exist with zero total copies).

# Must be ≥ available.

