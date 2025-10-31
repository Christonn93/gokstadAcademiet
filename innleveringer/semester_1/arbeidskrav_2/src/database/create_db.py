import os
from mysql.connector import Error

from src.database.connect_db import connect_db


def create_db(files: list[str] = None):
    """Create and initialize database using provided SQL files"""

    # Check if files were provided
    if not files:
        print("No SQL files provided.\n")
        return

    conn, cursor = connect_db()
    if conn is None or cursor is None:
        print("Failed to establish database connection. Cannot create database.\n")
        return

    # Loop through each SQL file
    try:
        for filename in files:
            print(f"Opening {filename}")

            # Validate file path
            if not os.path.exists(filename):
                print(f"File not found: {filename}\n")
                continue

            # Read SQL file content
            with open(filename, "r", encoding='utf-8') as file:
                sql_script = file.read()

            # Split and execute SQL statements
            for statement in sql_script.split(";"):
                if statement.strip():
                    cursor.execute(statement)

            print(f"Finished executing {filename}\n")

        # Commit database changes
        conn.commit()
        print(f"Database created successfully!\n")

    # Handle MySQL errors
    except Error as e:
        print(f"MySQL error: {e}\n")

    finally:
        # Close connection
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()