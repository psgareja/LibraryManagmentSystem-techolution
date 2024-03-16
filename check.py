#@Checkout class
class Checkout:
    @staticmethod
    def checkout_book(library, user_id, isbn):
        for book in library.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    library.save_books_to_file()
                    return True
                else:
                    return False
        return False

    @staticmethod
    def checkin_book(library, isbn):
        for book in library.books:
            if book.isbn == isbn:
                book.available = True
                library.save_books_to_file()
                return True
        return False