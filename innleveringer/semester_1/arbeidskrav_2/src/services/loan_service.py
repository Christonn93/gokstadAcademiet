from src.database.query_db import query_db

def register_loan(db_conn, lnr, isbn, eksnr, date):
    """Register a new loan for a borrower"""
    # Insert a new record into the loan table with borrower and book details
    query = "INSERT INTO loan (LNr, ISBN, EksNr, Utlaansdato) VALUES (%s, %s, %s, %s)"
    params = (lnr, isbn, eksnr, date)
    return query_db(query, db_conn, params)

def return_book(db_conn, utlansnr):
    """Mark a loan as returned by updating the return date"""
    # Update the loan record with the current date as the return date
    query = "UPDATE loan SET InnlevertDato = CURDATE() WHERE UtlaansNr = %s"
    params = (utlansnr,)
    return query_db(query, db_conn, params)

def get_borrower_history(db_conn, lnr):
    """Retrieve a borrower’s loan history"""
    # Select all loans associated with a specific borrower ID
    query = "SELECT * FROM loan WHERE LNr = %s"
    params = (lnr,)
    return query_db(query, db_conn, params)
