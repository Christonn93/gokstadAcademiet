from utils.handlers.db_handler import execute_query

def register_loan(db_conn, lnr, isbn, eksnr, date):
    query = "INSERT INTO loan (LNr, ISBN, EksNr, Utlaansdato) VALUES (%s, %s, %s, %s)"
    params = (lnr, isbn, eksnr, date)
    return execute_query(query, db_conn, params)

def return_book(db_conn, utlansnr):
    query = "UPDATE loan SET InnlevertDato = CURDATE() WHERE UtlaansNr = %s"
    params = (utlansnr,)
    return execute_query(query, db_conn, params)

def get_borrower_history(db_conn, lnr):
    query = "SELECT * FROM loan WHERE LNr = %s"
    params = (lnr,)
    return execute_query(query, db_conn, params)