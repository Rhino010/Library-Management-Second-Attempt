# Creation of a class named Book to hold a books title, the author, the genre, the publication year, and set its original
# availability to True under the assumption that a book will not be entered into the program until they have it.
class Book:
    def __init__(self, title, author, genre, publication_year):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_year = publication_year
        self.availability = True
# Retrieves the title from an instance of the Book class
    def get_title(self):
        return self.__title
# Retrieves an author from a Book class instance
    def get_author(self):
        return self.__author
# Retrieves the genre from a Book Class instance
    def get_genre(self):
        return self.__genre
# Retrieves the publication year from a Book class instance
    def get_publication_year(self):
        return self.__publication_year
# Method to toggle the availability of a book when called without needing explicit True or False inputs from user
    def set_availability(self):
        if not self.availability:
            self.availability = True
        else:
            self.availability = False
# Method to return a specific books avaialability. False means unavailable while True is available.
    def get_availability(self):
        return self.availability
# Method to display all books from a given instance.
    def show_all_books(self):
        if self.availability == True:
            print(f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Publish Year: {self.__publication_year}, Available: 'YES'")
        else:
            print(f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Publish Year: {self.__publication_year}, Available: 'NO'")
    
# Declaration of a library books dictionary to hold all books and information from a given instance of the Book class
library_books = {}
# Function to add a book to library_books dictionary
def add_book():
    title = input("What is the title of the book?\n")
    author = input("Who is the book's author?\n")
    genre = input("What genre is this book?\n")
    year = input("What is the publication year?\n")
    new_book = Book(title, author, genre, year)
    library_books[title] = new_book
    print(f"'{title}' has been successfully added.")

# Function to reset a books availability to False in the library_books dictionary
def borrow_book(book_to_borrow):
    if book_to_borrow in library_books and library_books[book_to_borrow].get_availability() == True:
        library_books[book_to_borrow].set_availability()
        print(f"You have successfully checked out '{book_to_borrow}' by {library_books[book_to_borrow].get_author()}")
    elif book_to_borrow in library_books and library_books[book_to_borrow].get_availability() == False:
        print("That book is currently checked out. Please try again at a later date.")
    else:
        print("We do not currently carry that title.")
# Function to set the availability to True for a book after function is called
def return_book(book):
    try:
        if book in library_books and library_books[book].get_availability() == False:
            library_books[book].set_availability()
        elif book not in library_books:
            print("Sorry that book does not belong to this library.")
    except Exception as e:
        print(f"Error occurred: {e}")
# Function to finc a particular book in the dictionary library_books and show whether it is currently available or not.
def find_book():
    try:
        book = input("What is the book title?\n")
        if book in library_books and library_books[book].get_availability() == True:
            print(f"Book: {book}, Available to check out: 'YES' ")
        elif book in library_books and library_books[book].get_availability() == False:
            print(f"Book: {book}, Available to check out: 'NO' ")
        else:
            print("This library does not carry that title.")
    except Exception as e:
        print(f"Error occurred: {e}")
# Function to print out all the books in the library_books dictionary and display all books with all information had on them.
def show_all_books():
    if not library_books:
        print("No books currently in the library.")
    else:
        print("\nHere is a list of books we keep:")
        for book in library_books.values():
            book.show_all_books()



