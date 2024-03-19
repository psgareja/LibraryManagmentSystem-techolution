
# **Library Management System**


The Library Management System is a software application designed to help libraries efficiently manage their collection of books and users.


## **Features**


**Book Management**: Add, update, delete, list, and search books by various attributes such as title, author, or ISBN.

**User Management**: Add, update, delete, list, and search users by attributes like name or user ID.

**Check-out and Check-in**: Allow users to check out and check in books.

**Book Availability**: Track the availability of books in the library.

**Simple Logging**: Log operations performed within the system.


## **Architecture**

The system is designed with the following components:


**main.py**: Contains the main execution logic and user interface.

**book.py**: Defines the Book class and related methods for book management.

**user.py**: Defines the User class and related methods for user management.

**checkout.py**: Contains functionality for checking out books.

**checkin.py**: Contains functionality for checking in books.

**storage.py**: Defines the Storage class for file-based storage operations.

**models.py**: Defines the data models used in the application.


## **Code Structure:**


.

├── main.py

├── book.py

├── user.py

├── checkout.py

├── checkin.py

├── storage.py

├── managment.py

├── README.md

├── books.json

└── users.json


## **Installation**

**1.Clone the repository:**

git clone https://github.com/psgareja/LibraryManagmentSystem-techolution.git

**2.Navigate to the project directory:**

cd LibraryManagmentSystem-techolution

**3.Usage:**

Run the main.py file to start the program:

python main.py

