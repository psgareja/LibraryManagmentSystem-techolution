#@Book Information
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.isbn}, {'Available' if self.available else 'Not Available'})"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["isbn"])