from book import Book
from user import User
from storage import Storage
from library import Library
from check import Checkout

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Books")
    print("4. Add User")
    print("5. Remove User")
    print("6. Search Users")
    print("7. Checkout Book")
    print("8. Checkin Book")
    print("9. List Book")
    print("10. Exit")
    choice = input("Enter your choice: ")
    return choice
    
#@Main function 
def main():
    book_storage = Storage('books.json')
    user_storage = Storage('users.json')

    library = Library(book_storage, user_storage)
    library.load_books_from_file()
    library.load_users_from_file()

    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)
            print("Book added.")
        elif choice == '2':
            isbn = input("Enter ISBN of book to remove: ")
            if library.remove_book(isbn):
                print("Book removed.")
            else:
                print("Book not found.")
        elif choice == '3':
            keyword = input("Enter keyword to search: ")
            results = library.search_books(keyword)
            if results:
                print("Search results:")
                for book in results:
                    print(book)
            else:
                print("No matching books found.")
        elif choice == '4':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            library.add_user(name, user_id)
            print("User added.")
        elif choice == '5':
            user_id = input("Enter user ID of user to remove: ")
            if library.remove_user(user_id):
                print("User removed.")
            else:
                print("User not found.")
        elif choice == '6':
            keyword = input("Enter keyword to search: ")
            results = library.search_users(keyword)
            if results:
                print("Search results:")
                for user in results:
                    print(user)
            else:
                print("No matching users found.")
        elif choice == '7':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            if Checkout.checkout_book(library, user_id, isbn):
                print("Book checked out.")
            else:
                print("Book not available or ISBN/user ID incorrect.")
        elif choice == '8':
            isbn = input("Enter ISBN of the book to checkin: ")
            if Checkout.checkin_book(library, isbn):
                print("Book checked in.")
            else:
                print("Book with given ISBN not found.")
        elif choice == '9':
            library.list_books()
        elif choice == '10':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()