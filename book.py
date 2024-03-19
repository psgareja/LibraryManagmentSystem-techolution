#@Book Information
class Book:
    #@Constructor method to initialize a Book object with given title, author, and ISBN.
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    #@__repr__(): Returns a string representation of the Book object.
    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.isbn}, {'Available' if self.available else 'Not Available'})"

    #@to_dict(): Converts the Book object into a dictionary representation.
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }
        
    #@from_dict(data): Creates a Book object from a dictionary.
    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["isbn"])