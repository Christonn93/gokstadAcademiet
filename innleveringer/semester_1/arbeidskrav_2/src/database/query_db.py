from database import connect_db

"""
This module contains reusable database querying functions.

Resources used to build the solution:

https://www.freecodecamp.org/news/connect-python-with-sql/
https://ia800902.us.archive.org/4/items/2018PythonNotesForProfessionals/2018_python-notes-for-professionals.pdf
https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html

"""

def query_db(sql_query: str, params=None, fetch=True):
    """Execute a SQL query and return results from the database."""

    try:
        conn, cursor = connect_db()
        if conn is None or cursor is None:
            print("❌ Failed to establish database connection. Query aborted.\n")
            return None

        cursor = conn.cursor(dictionary=True)

        # Execute query — if params is None, pass an empty tuple
        cursor.execute(sql_query, params or ())

        # SELECT queries → fetch results
        if fetch:
            results = cursor.fetchall()
            return [row for row in results]  # simple copy of results list

        # Non-SELECT queries → commit and return affected rows
        conn.commit()
        return cursor.rowcount

    except Exception as e:
        print(f"❌ Error executing query: {e}")
        return None

