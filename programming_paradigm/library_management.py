"""

3. Implementing Basic OOP for a Library Management System
mandatory
Objective: Solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.

Your Task: library_management.py
Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.
Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.
Provided for Testing: main.py
This script demonstrates how to interact with your Book and Library classes.

from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
Expected Outputs for Each Step in main.py:
After Initial Setup:
   Available books after setup:
   Brave New World by Aldous Huxley
   1984 by George Orwell
After Checking Out ‘1984’:
   Available books after checking out '1984':
   Brave New World by Aldous Huxley
After Returning ‘1984’:
   Available books after returning '1984':
   Brave New World by Aldous Huxley
   1984 by George Orwell
Note for you:
Your Book class should provide methods to check a book out and return it, affecting its availability.
Your Library class needs to manage a collection of books, including adding new books to the collection, checking a book out (which marks it as unavailable), returning it (making it available again), and listing all available books.
Implementing these functionalities requires careful thought about how objects interact with each other in terms of state and behavior.
Use the provided main.py for testing your implementation. The expected outputs give you a clear indication of how your program should behave if implemented correctly.

"""

class Book:
    def __init__(self, title, author, is_checked_out = False):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out


    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book : Book):
        self._books.append(book)
        print(self._books)
    
    def check_out_book(self, book : Book):
        self._books.remove(book)
        return self._books
    
    
    def return_book(self, book : Book):
        self._books.append(book)
        return self._books
    

    def list_available_books(self):
        return [str(book) for book in self._books]
        

book = Book("1984", "Alee")

library = Library()


print("\n--------Adding Book----------")
library.add_book(book)

print("\n--------Checkout a Book----------")
library.check_out_book(book)

print("\n--------Return a Book----------")
library.return_book(book)

print("\n--------List Available Books----------")
library.list_available_books()


