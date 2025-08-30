# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0
    
    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books = len(self.books)

    def get_no_of_books(self):
        return self.no_of_books

    def print_books(self):
        if self.no_of_books == 0:
            print("No books in the library yet!")
        else:
            print("Books in the library:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")


my_library = Library()


my_library.add_book("Harry Potter")
my_library.add_book("Game Of Thrones")
my_library.add_book("Sherlock Holmes")

my_library.print_books()

print(f"This Library has {my_library.get_no_of_books()} books")