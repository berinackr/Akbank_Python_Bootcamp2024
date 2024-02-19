import os

class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self, option='normal'):
        self.file.seek(0)
        books = self.file.read().splitlines()

        if option == 'title_alphabetical':
            books.sort(key=lambda x: x.split(',')[0])
        elif option == 'author_alphabetical':
            books.sort(key=lambda x: x.split(',')[1])

        print("\n~ List of Books ~")
        for book in books:
            title, author = book.split(',')[:2]
            print(f"Title: {title}, Author: {author}")
        print("\n")

    def add_book(self):
        print("\n ~ Add Book ~")
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        book_release_year = input("Enter first release year: ")
        book_num_pages = input("Enter number of pages: ")
        print("\n")

        self.file.write(book_title + "," + book_author + "," + book_release_year + "," + book_num_pages + "\n")

    def remove_books(self):
        title = input("Enter the title of the book to remove: ")
        temp_file = open("temp.txt", "w")
        self.file.seek(0)
        for book in self.file:
            if not book.startswith(title):
                temp_file.write(book)
        temp_file.close()
        self.file.close()
        os.remove("books.txt")
        os.rename("temp.txt", "books.txt")
        self.file = open("books.txt", "a+")
        print("\n\n")

    def search_book(self):
        title = input("Enter the title of the book to search: ")
        self.file.seek(0)  # Move the cursor to the beginning of the file
        found = False
        for line in self.file:
            book_info = line.strip().split(',')
            if book_info[0] == title:
                print(f"Title: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Number of Pages: {book_info[3]}\n\n")
                found = True
                break
        if not found:
            print("Book not found.\n\n")

lib = Library()

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Search book")
    print("Q) Exit")
    choice = input("Enter your choice : ")
    selected = 0

    if choice == '1':
        print("\n")
        print("* List option *")
        print("1) List as in file")
        print("2) List alphabetically by title")
        print("3) List alphabetically by author")
        selected = input("Enter your choice : ")
        if selected == '1':
            lib.list_books()
            continue
        elif selected == '2':
            lib.list_books(option='title_alphabetical')
            continue
        elif selected == '3':
            lib.list_books(option='author_alphabetical')
            continue
        else:
            print("Invalid choice. Please choose again.\n")
            continue
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_books()
    elif choice == '4':
        lib.search_book()
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Please choose again.")
