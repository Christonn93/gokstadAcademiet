from innleveringer.semester_1.arbeidskrav_2.python.app.menu import prompt_for_return, prompt_for_loan_details, \
    prompt_for_history
from innleveringer.semester_1.arbeidskrav_2.python.services.book_service import get_all_books, search_books
from innleveringer.semester_1.arbeidskrav_2.python.services.loan_service import register_loan, return_book, \
    get_borrower_history
from innleveringer.semester_1.arbeidskrav_2.python.utils.handlers.error_handler import handle_error
from innleveringer.semester_1.arbeidskrav_2.python.utils.helpers.formatters import print_books_table, print_history


def handle_user_choice(choice, db_conn):
    try:
        if choice == 1:
            books = get_all_books(db_conn)
            print_books_table(books)

        elif choice == 2:
            keyword = input("Enter a title or author to search: ")
            results = search_books(db_conn, keyword)
            print_books_table(results)

        elif choice == 3:
            lnr, isbn, eksnr, date = prompt_for_loan_details()
            result = register_loan(db_conn, lnr, isbn, eksnr, date)
            print(result)

        elif choice == 4:
            utlansnr = prompt_for_return()
            result = return_book(db_conn, utlansnr)
            print(result)

        elif choice == 5:
            lnr = prompt_for_history()
            history = get_borrower_history(db_conn, lnr)
            print_history(history)

        elif choice == 6:
            print("Exiting program. Goodbye!")
            return False

        else:
            print("Invalid choice. Please try again.")

        return True

    except Exception as e:
        handle_error(e)
        return True
