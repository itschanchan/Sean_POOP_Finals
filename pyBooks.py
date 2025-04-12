from abc import ABC, abstractmethod

# Abstract base class for Author and Pages
class Book(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, value):
        pass

# Author class inheriting from Book
class Author(Book):
    def __init__(self, author_name):
        self.author_name = author_name

    def __eq__(self, value):
        return isinstance(value, Author) and self.author_name == value.author_name

    def __str__(self):
        return self.author_name

class Pages(Book):
    def __init__(self, page_count):
        self.page_count = page_count

    def __str__(self):
        return str(self.page_count)

    def __eq__(self, value):
        return isinstance(value, Pages) and self.page_count == value.page_count

# BookDetails class
class BookDetails:
    def __init__(self, title, author_name, page_count):
        self.title = title
        self.author = Author(author_name)
        self.pages = Pages(page_count)

    def __eq__(self, value):
        return self.title == value.title or self.author == value.author

    def display_details(self):
        return f'Book Title: {self.title},\nAuthor: {self.author},\nPage Count: {self.pages}'

    def __str__(self):
        return f'"{self.title}" by {self.author}'

    # Class method for adding books in the dictionary
    @classmethod
    def add_book(cls, data):
        return cls(data["title"], data["author"], data["pages"])

# Book Instances
book_1 = BookDetails('The Great Gatsby', 'F. Scott Fitzgerald', 180)
book_2 = BookDetails('Kafka on the Shore', 'Haruki Murakami', 512)
book_3 = BookDetails('Dune', 'Frank Herbert', 412)
book_4 = BookDetails('Rainbow Six', 'Tom Clancy', 912)
book_5 = BookDetails('The Hunt for Red October', 'Tom Clancy', 387)

# Adding a book using class method
book_data = {
    "title": "Norwegian Wood",
    "author": "Haruki Murakami",
    "pages": 296
}
book_6 = BookDetails.add_book(book_data)

# Outputs
print(f"The book that I'm interested:\n{book_2.display_details()}")
print(f'\nIs "{book_4.title}" and "{book_5.title}" have the same author? {book_4 == book_5}')
print(f'\nBook added from the class method:\n{book_6.display_details()}')
