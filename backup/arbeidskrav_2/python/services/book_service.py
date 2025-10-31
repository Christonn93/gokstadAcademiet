from utils.handlers.db_handler import execute_query

def get_all_books(db_conn):
    return execute_query("SELECT * FROM book", db_conn)

def search_books(db_conn, keyword):
    query = "SELECT * FROM book WHERE title LIKE %s OR author LIKE %s"
    params = (f"%{keyword}%", f"%{keyword}%")
    return execute_query(query, db_conn, params)