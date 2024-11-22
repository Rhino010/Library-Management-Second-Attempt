class Author:
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio

    def set_name(self, new_name):
        self.name = new_name
    
    def get_name(self):
        return self.name

    def set_bio(self, new_bio):
        self.bio = new_bio

    def get_bio(self):
        return self.bio

authors = {}

def add_author():
    name = input("Enter the author's name:\n")
    bio = input("Enter some information about the author:\n")
    temp_author = Author(name, bio)
    new_bio = temp_author.get_bio()
    authors[name] = new_bio
    print(authors)

def find_author(authors):
    author = input("Please type the author's name you are looking for:\n")
    if author in authors:
        print(f"{authors[author]}, {authors[author][-1]}")

def show_all_authors(authors):
    for author in authors:
        print(f"Author Name: {author}, Bio: {author[author][-1]}")

add_author()