from services import BookService, LoanService, BorrowerService
from utils.helpers.formatting.format_table import format_table

def query_program():
    """Interactive query program for the library system."""
    book_service = BookService()
    loan_service = LoanService()
    borrower_service = BorrowerService()

    while True:
        print("\n📚 === Library Query Menu ===")
        print("1️⃣ Get all books published after year 2000")
        print("2️⃣ Get author + title of all books (A-Z by author)")
        print("️3️⃣ Get all books with more than 300 pages")
        print("️4️⃣ Add a new book to the 'bok' table")
        print("️5️⃣ Add a new borrower to the 'låner' table")
        print("️6️⃣ Update a borrower’s address")
        print("️7️⃣ Get all loans (with borrower + book info)")
        print("️8️⃣ Get all books and number of copies per book")
        print("️9️⃣ Get number of loans per borrower")
        print("🔟 Get number of loans per book")
        print("1️⃣1️⃣ Get books that have not been loaned")
        print("1️⃣2️⃣ Get authors and their number of loaned books")
        print("0️⃣ Exit")

        choice = input("\n➡️  Enter your choice: ").strip()

        if choice == "1":
            results = book_service.get_books_after_year(2000)
            print("\n" + format_table(results))

        elif choice == "2":
            results = book_service.get_books_sorted_by_author()
            print("\n" + format_table(results))

        elif choice == "3":
            results = book_service.get_books_by_page_count(300)
            print("\n" + format_table(results))

        elif choice == "4":
            print("\n🆕 Add a New Book")
            isbn = input("ISBN: ")
            title = input("Title: ")
            author = input("Author: ")
            publisher = input("Publisher: ")
            year = input("Publication Year: ")
            pages = input("Number of Pages: ")
            book_service.add_new_book(isbn, title, author, publisher, year, pages)
            print("\n✅ Book added successfully.")

        elif choice == "5":
            print("\n🆕 Add a New Borrower")
            borrower_id = input("Borrower ID (LNr): ")
            name = input("Name: ")
            address = input("Address: ")
            borrower_service.add_new_borrower(borrower_id, name, address)
            print("\n✅ Borrower added successfully.")

        elif choice == "6":
            print("\n✏️  Update Borrower Address")
            borrower_id = input("Borrower ID (LNr): ")
            new_address = input("New Address: ")
            borrower_service.update_borrower_address(borrower_id, new_address)
            print("\n✅ Address updated successfully.")

        elif choice == "7":
            results = loan_service.get_all_loans_with_details()
            print("\n" + format_table(results))

        elif choice == "8":
            results = book_service.get_books_with_copy_count()
            print("\n" + format_table(results))

        elif choice == "9":
            results = loan_service.get_loan_count_per_borrower()
            print("\n" + format_table(results))

        elif choice == "10":
            results = loan_service.get_loan_count_per_book()
            print("\n" + format_table(results))

        elif choice == "11":
            results = book_service.get_books_not_loaned()
            print("\n" + format_table(results))

        elif choice == "12":
            results = loan_service.get_loaned_books_per_author()
            print("\n" + format_table(results))

        elif choice == "13":
            results = book_service.get_all_books()
            print("\n" + format_table(results))

        elif choice == "0":
            print("\n👋 Exiting program. Goodbye!")
            break

        else:
            print("⚠️  Invalid choice, please try again.")
