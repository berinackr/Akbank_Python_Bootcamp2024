# Library Management System

This is a simple library management system implemented in Python. It allows users to list, add, remove, and search for books in a library.

## Files

- `library.py`: Contains the implementation of the Library class and the main menu for interacting with the library.
- `books.txt`: Stores the information about books in the library.

## Class: Library

### Methods:

- `__init__(self)`: Initializes the Library object and opens the `books.txt` file for reading and appending.
- `__del__(self)`: Closes the `books.txt` file when the Library object is deleted.
- `list_books(self, option='normal')`: Lists the books in the library. The listing can be normal, alphabetical by title, or alphabetical by author.
- `add_book(self)`: Adds a new book to the library.
- `remove_books(self)`: Removes a book from the library.
- `search_book(self)`: Searches for a book by title in the library.

## Usage

1. Run the `library.py` file.
2. Follow the on-screen instructions to perform various operations such as listing books, adding a book, removing a book, searching for a book, or exiting the program.

## Notes

- When adding a book, you need to enter the title, author, release year, and number of pages.
- When removing a book, you need to enter the title of the book to be removed.
- When searching for a book, you need to enter the title of the book to be searched.
