from book import Book
from user import User
import json
class Library:
    def __init__(self, book_storage, user_storage):
        self.books = []
        self.users = []
        self.book_storage = book_storage
        self.user_storage = user_storage

    def load_books_from_file(self):
        book_data = self.book_storage.load_data()
        self.books = [Book.from_dict(data) for data in book_data]

    def load_users_from_file(self):
        user_data = self.user_storage.load_data()
        self.users = [User.from_dict(data) for data in user_data]

    def save_books_to_file(self):
        data = [book.to_dict() for book in self.books]
        self.book_storage.save_data(data)

    def save_users_to_file(self):
        data = [user.to_dict() for user in self.users]
        self.user_storage.save_data(data)

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save_books_to_file()

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_books_to_file()
                return True
        return False

    def search_books(self, keyword):
        return [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower() or keyword.lower() in book.isbn.lower()]

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user)
        self.save_users_to_file()

    def remove_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                self.save_users_to_file()
                return True
        return False

    def search_users(self, keyword):
        return [user for user in self.users if keyword.lower() in user.name.lower() or keyword.lower() == user.user_id.lower()]

    def list_books(self):
        try:
            with open("book.json", "r") as file:
                books = json.load(file)
                if not books:
                    print("No books available.")
                else:
                    print("List of all books:")
                    for book in books:
                        print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Available: {'Yes' if book['available'] else 'No'}")
        except FileNotFoundError:
            print("Book database not found.")