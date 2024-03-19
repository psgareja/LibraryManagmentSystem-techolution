from book import Book
from user import User
import json
class Library:
    #@books: A list of Book objects representing the books in the library.
    #@users: A list of User objects representing the users of the library.
    def __init__(self, book_storage, user_storage):
        self.books = []
        self.users = []
        self.book_storage = book_storage
        self.user_storage = user_storage

    #@load_books_from_file(self): Loads book data from file and populates the books list.
    def load_books_from_file(self):
        book_data = self.book_storage.load_data()
        self.books = [Book.from_dict(data) for data in book_data]

    #@load_users_from_file(self): Loads user data from file and populates the users list.
    def load_users_from_file(self):
        user_data = self.user_storage.load_data()
        self.users = [User.from_dict(data) for data in user_data]

    #@save_books_to_file(self): Saves book data to file.
    def save_books_to_file(self):
        data = [book.to_dict() for book in self.books]
        self.book_storage.save_data(data)

    #@save_users_to_file(self): Saves user data to file.
    def save_users_to_file(self):
        data = [user.to_dict() for user in self.users]
        self.user_storage.save_data(data)

    #@add_book(self, book): Adds a book to the library.
    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save_books_to_file()

    #@remove_book(self, isbn): Removes a book from the library based on its ISBN.
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_books_to_file()
                return True
        return False

    #@search_users(self, keyword): Searches for users in the library based on a keyword (name or user ID).
    def search_books(self, keyword):
        return [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower() or keyword.lower() in book.isbn.lower()]
   
    #@add_user(self, book): Adds a user to the database.
    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user)
        self.save_users_to_file()

    #@remove_user(self, user_id): Removes a user from the library based on their user ID.
    def remove_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                self.save_users_to_file()
                return True
        return False

    #@search_users(self, keyword): Searches for users in the library based on a keyword (name or user ID).
    def search_users(self, keyword):
        return [user for user in self.users if keyword.lower() in user.name.lower() or keyword.lower() == user.user_id.lower()]

    #@list_books(self): Lists all available books in the library.
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