# Imports from all files to incorporate all classes and functionality into main.py
from book import Book, add_book, borrow_book, return_book, find_book, show_all_books
from user import User, add_user, show_all_users, view_user_details, user_borrowed_books, user_book_return
from author import Author, add_author, find_author, show_all_authors
import os

def main():
    while True:
        try:
            invalid = "Invalid selection, please try again."

            print("--Main Menu--\nPlease select from the following options:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit Program")
            choice = input("Please choose the number of your selection.\n")

            if choice == '1':
                os.system('cls||clear')
                print("--Book Operations Menu--\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
                selection = input("Please select from the above menu:\n")
                if selection == '1':
                    add_book()
                elif selection == '2':
                    book_borrowed = input("What book will you be checking out?\n")
                    user_borrowed_books(book_borrowed)
                    borrow_book(book_borrowed)
                elif selection == '3':
                    book_returned = input("What book will you be returning?\n")
                    return_book(book_returned)
                    user_book_return(book_returned)
                elif selection == '4':
                    find_book()
                elif selection == '5':
                    show_all_books()
                else:
                    print(invalid)

            elif choice == '2':
                os.system('cls||clear')
                print("--User Operations--\n1. Add a new user\n2. View User Details\n3. Display all users")
                selection = input("Please select from the above menu:\n")
                if selection == '1':
                    add_user()
                elif selection == '2':
                    view_user_details()
                elif selection == '3':
                    show_all_users()
                else:
                    print(invalid)

            elif choice == '3':
                os.system('cls||clear')
                print("--Author Operations--\n1. Add a new author\n2. View author details\n3. Display all authors")
                selection = input("Please select from the above menu:\n")
                if selection == '1':
                    add_author()
                elif selection == '2':
                    find_author()
                elif selection == '3':
                    show_all_authors()
                else:
                    print(invalid)

            elif choice == '4':
                os.system('cls||clear')
                print("Shutting down......")
                break
            else:
                print(invalid)
        
        except Exception as e:
            print(f"Unexcpected error: {e}")

if __name__ == "__main__":
    main()

# TODO: Add a txt file to write the information to.