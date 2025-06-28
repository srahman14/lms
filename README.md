## Library Management System (LMS)

### What it is:

A system to manage a library’s collection of books, user membership, lending (loans), returns, and fine tracking. 

### Core OOP Design:

- **Book**: Attributes like title, author, ISBN, publication year, copies available.
- **Member**: User who can borrow books. Attributes: member ID, name, contact info, membership date, outstanding fines.
- **Loan**: Tracks which book is loaned to which member, loan date, due date, return date.
- **Librarian**: Admin role managing books and members.
- **Catalog**: Collection of books; methods to search, add, update, remove books.
- **Fine**: Calculates overdue fines based on due date and return date.
- **LibrarySystem** (controller): manages members, loans, fines, and overall logic.
