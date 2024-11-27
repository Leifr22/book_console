Book Console Application
This application is a simple console-based library management system for managing books. It allows users to add, delete, search, list, and update the status of books in a library. The data is stored in a JSON file for persistence.

Features
Add a Book

Allows the user to input the title, author, and publication year of a book.
Automatically generates a unique ID and sets the book's status to "в наличии" (available).
Remove a Book

Deletes a book from the library using its unique ID.
Handles errors when the ID does not exist.
Search for a Book

Enables searching by title, author, or publication year.
Case-insensitive search.
List All Books

Displays all books in the library with their details:
ID
Title
Author
Year
Status
Update Book Status

Updates the status of a book (e.g., "в наличии" (available) or "выдана" (checked out)).
Handles invalid status values and non-existent book IDs.
Data Persistence

Stores book data in a library.json file.
Automatically loads data when the application starts.
Requirements
Python 3.10 or higher.
No additional libraries are required.
File Structure
book_console.py: Main application file containing all logic.
library.json: File used for data storage (auto-generated if it doesn’t exist).
Usage
Run the application using the following command:

python book_console.py

Follow the on-screen menu to perform actions:

Add a book
Remove a book
Search for a book
List all books
Update book status
Exit
Error Handling
Handles incorrect input formats (e.g., non-integer IDs or years).
Ensures smooth operation when performing actions on non-existent books.
Notes
The application interface is in Russian.
Status options are:
"в наличии" (available)
"выдана" (checked out)
To reset the library, delete the library.json file.
Future Enhancements (Optional)
Add support for multilingual interfaces.
Improve search functionality with partial matches.
Implement a graphical user interface (GUI) or web-based interface.
This application is a great starting point for managing a digital book library through a command-line interface!