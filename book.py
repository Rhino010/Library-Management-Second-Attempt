class Book:
    def __init__(self, title, author, genre, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.availability = True

    def get_title(self):
        return self.title
    
    def set_title(self, new_title):
        self.title = new_title


book1 = Book("1984", "Orwell", "SciFI", "1965")  
print(book1.get_title())
book1.set_title("Hello")
print(book1.get_title())