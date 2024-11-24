# Initialize a User class
class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.borrowed_books = []
# Method to set an user id
    def set_id(self, new_id):
        self.__id = new_id
# Method to get the user id
    def get_id(self):
        return self.__id
# Method to set user name
    def set_name(self, new_name):
        self.__name = new_name
# Method to return the value of the user's name
    def get_name(self):
        return self.__name
# Accesses self.borrowed_books to be recalled for the user
    def get_users_books(self):
        return self.borrowed_books
# Method to add to the list of borrowed books
    def add_to_borrowed(self, book):
        self.borrowed_books.append(book)
    

    
# Declared user variable as a dictionary to track users and information about the user
users = {}

# Function to prompt the user for a user's information
def add_user():
    user_id = input("Please give the user's ID number:\n")
    user_name = input("Please enter the user's name:\n")
    new_user = User(user_id, user_name)
    users[user_id] = new_user
    print(f"User with ID: {user_id} and Name: {user_name} has been added.")
# Function to print out all of a selected user's information
def view_user_details():
    try:
        user_id = input("What is the users ID number?\n")
        if user_id in users:
            user_obj = users[user_id]
            print(f"User found, ID: {user_obj.get_id()}, Name: {user_obj.get_name()}, Checked out books: {user_obj.get_users_books()}")
    except Exception as e:
        print(f"Unexpected error: {e}")
# Function to print out all users currently held in the user dictionary
def show_all_users():
    if not users:
        print("There are no users at this time.")
    else:
        for id, user_obj in users.items():
            print(f"User ID: {id}, Name: {user_obj.get_name()}, Borrowed Books: {user_obj.get_users_books()}")

# Function to add a book to each instance of a user when checking out a book with the given user's id number
def user_borrowed_books(book):
    user_id = input("Please give the user's ID number:\n")
    if user_id not in users:
        print("That user does not exist.")
    else:
        user_obj = users[user_id]
        user_obj.add_to_borrowed(book)




