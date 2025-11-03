from src.services.book_service import get_all_books, search_books
from src.services.loan_service import register_loan, return_book, get_borrower_history
from depricated_code.prompts.prompt_for_history import prompt_for_history
from interface import prompt_for_loan_details
from interface import prompt_for_return

def handle_user_choice(choice, database):
    """Handle user menu selections and execute corresponding database actions"""

    try:
        # Access active database connection
        db_conn = database.connection

        # Fetch and display all books
        if choice == 1:
            books = get_all_books(db_conn)
            print_books_table(books)

        # Search books by title or author
        elif choice == 2:
            keyword = input("Enter a title or author to search: ")
            results = search_books(db_conn, keyword)
            print_books_table(results)

        # Register a new book loan
        elif choice == 3:
            lnr, isbn, eksnr, date = prompt_for_loan_details()
            result = register_loan(db_conn, lnr, isbn, eksnr, date)
            print(result)

        # Return a borrowed book
        elif choice == 4:
            utlansnr = prompt_for_return()
            result = return_book(db_conn, utlansnr)
            print(result)

        # Display borrowing history for a user
        elif choice == 5:
            lnr = prompt_for_history()
            history = get_borrower_history(db_conn, lnr)
            print_history(history)

        # Exit the program
        elif choice == 6:
            print("Exiting program. Goodbye!")
            return False

        # Handle invalid menu input
        else:
            print("Invalid choice. Please try again.")

        # Continue running after handling a valid choice
        return True

    # Handle unexpected errors gracefully
    except Exception as e:
        print(e)
        return True
