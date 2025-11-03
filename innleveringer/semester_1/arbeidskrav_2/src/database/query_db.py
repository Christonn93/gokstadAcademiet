from database import connect_db

"""
This module contains reusable database querying functions.

Resources used to build the solution:

https://www.freecodecamp.org/news/connect-python-with-sql/
https://ia800902.us.archive.org/4/items/2018PythonNotesForProfessionals/2018_python-notes-for-professionals.pdf
https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html

"""


def query_db(sql_query: str, params=None, fetch=True):
    """Execute a SQL query and return results from the database"""

    try:
        # Establish a database connection (reuse an existing connection or create a new one)
        conn, cursor = connect_db()
        if conn is None or cursor is None:
            print("Failed to establish database connection. Cannot create database.\n")
            return None

        cursor = conn.cursor(dictionary=True)

        # Execute the query using cursor.execute()
        # if params is None, pass an empty tuple so the driver doesn’t choke.
        cursor.execute(sql_query, params or ())

        # If it's a SELECT query, fetch the results (fetchone, fetchall, etc.)
        if fetch:
            results = cursor.fetchall()

            # Initialise empty list
            from_db = []

            # Loop over the results and append them into our list
            # Returns a list of tuples (or dicts if dictionary=True is used in cursor)
            for result in results:
                from_db.append(result)

            return from_db

        # If it's an INSERT, UPDATE, or DELETE query, commit the changes
        else:
            conn.commit()
            # Return how many rows were affected
            return cursor.rowcount

    except Exception as e:
        # Handle potential MySQL errors with try/except for Error
        print(f"OBS!! An error in the query_db have decided to present itself: {e}")
        return None

