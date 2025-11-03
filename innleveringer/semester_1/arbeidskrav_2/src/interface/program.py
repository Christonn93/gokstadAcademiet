from services import BookService, LoanService, BorrowerService
from utils.helpers.formatting.format_table import format_table

def query_program():
    """Interactive query program for the library system."""
    book_service = BookService()
    loan_service = LoanService()
    borrower_service = BorrowerService()

    while True:
        print("\nChoose a query to execute:")
        print("1. Get all books published after year 2000")
        print("2. Get author and title of all books, sorted alphabetically by author")
        print("3. Get all books with more than 300 pages")
        print("4. Add a new book to the 'bok' table")
        print("5. Add a new borrower to the 'låner' table")
        print("6. Update address for a specific borrower")
        print("7. Get all loans with borrower name and book title")
        print("8. Get all books and number of copies per book")
        print("9. Get number of loans per borrower")
        print("10. Get number of loans per book")
        print("11. Get all books that have not been loaned out")
        print("12. Get author and number of loaned books per author")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            results = book_service.get_books_after_year(2000)
            print("\n", format_table(results))

        elif choice == "2":
            results = book_service.get_books_sorted_by_author()
            print("\n", format_table(results))

        elif choice == "3":
            results = book_service.get_books_by_page_count(300)
            print("\n", format_table(results))


        elif choice == "4":
            print("\nAdd a new book:")
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            publisher = input("Enter publisher: ")
            year = input("Enter year of publication: ")
            pages = input("Enter number of pages: ")
            book_service.add_new_book(isbn, title, author, publisher, year, pages)
            print("\n✅ Book added successfully.")

        elif choice == "5":
            print("\nAdd a new borrower:")
            borrower_id = input("Enter borrower ID (LNr): ")
            name = input("Enter name: ")
            address = input("Enter address: ")
            borrower_service.add_new_borrower(borrower_id, name, address)
            print("\n✅ Borrower added successfully.")

        elif choice == "6":
            print("\nUpdate borrower address:")
            borrower_id = input("Enter borrower ID (LNr): ")
            new_address = input("Enter new address: ")
            borrower_service.update_borrower_address(borrower_id, new_address)
            print("\n✅ Address updated successfully.")

        elif choice == "7":
            results = loan_service.get_all_loans_with_details()
            print("\n", format_table(results))

        elif choice == "8":
            results = book_service.get_books_with_copy_count()
            print("\n", format_table(results))

        elif choice == "9":
            results = loan_service.get_loan_count_per_borrower()
            print("\n", format_table(results))

        elif choice == "10":
            results = loan_service.get_loan_count_per_book()
            print("\n", format_table(results))

        elif choice == "11":
            results = book_service.get_books_not_loaned()
            print("\n", format_table(results))

        elif choice == "12":
            results = loan_service.get_loaned_books_per_author()
            print("\n", format_table(results))

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, try again.")
