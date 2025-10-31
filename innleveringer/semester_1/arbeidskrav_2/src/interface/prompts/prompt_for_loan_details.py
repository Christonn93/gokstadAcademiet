def prompt_for_loan_details():
    """Prompt for details needed to register a new loan"""
    # Collect borrower ID, book info, and loan date
    print("\nRegistering a new loan:")
    lnr = input("Enter borrower ID (LNr): ")
    isbn = input("Enter book ISBN: ")
    eksnr = input("Enter copy number (EksNr): ")
    date = input("Enter loan date (YYYY-MM-DD): ")
    return lnr, isbn, eksnr, date