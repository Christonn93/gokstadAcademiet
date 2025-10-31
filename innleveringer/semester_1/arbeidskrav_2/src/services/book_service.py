from src.database.query_db import query_db


def get_all_books(db_conn):
    """Retrieve all books from the database"""
    # Execute a query to fetch all book records
    return query_db("SELECT * FROM book", db_conn)


def search_books(db_conn, keyword):
    """Search books by title or author keyword"""
    # Prepare a query using pattern matching for title and author
    query = "SELECT * FROM book WHERE title LIKE %s OR author LIKE %s"

    # Use wildcard parameters for partial search matches
    params = (f"%{keyword}%", f"%{keyword}%")

    # Execute query with parameters and return matching records
    return query_db(query, db_conn, params)
