def display_menu():
    print("\n📚 Library System Menu")
    print("1. View all books")
    print("2. Search for a book")
    print("3. Register a loan")
    print("4. Return a book")
    print("5. View borrower history")
    print("6. Exit")

def get_user_choice():
    try:
        choice = int(input("Enter your choice (1–6): "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number between 1–6.")
        return None

def prompt_for_loan_details():
    print("\nRegistering a new loan:")
    lnr = input("Enter borrower ID (LNr): ")
    isbn = input("Enter book ISBN: ")
    eksnr = input("Enter copy number (EksNr): ")
    date = input("Enter loan date (YYYY-MM-DD): ")
    return lnr, isbn, eksnr, date

def prompt_for_return():
    utlansnr = input("\nEnter loan number to mark as returned: ")
    return utlansnr

def prompt_for_history():
    lnr = input("\nEnter borrower ID (LNr) to view history: ")
    return lnr
