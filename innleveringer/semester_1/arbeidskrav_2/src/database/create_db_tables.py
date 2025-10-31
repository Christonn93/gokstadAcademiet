import os
from mysql.connector import Error

from src.database.connect_db import connect_db


def create_db_tables(files: list[str] = None):
    """Create database tables from provided SQL files"""

    # Using database connection
    conn, cursor = connect_db()

    # Check if connection failed
    if conn is None or cursor is None:
        print("No database connection\n")
        return

    # Check if files list is provided
    if not files:
        print("No SQL files provided to create tables.\n")
        cursor.close()
        conn.close()
        return

    try:
        # Loop through each SQL file and execute its statements
        for file_path in files:
            print(f"Creating table from: {file_path}")

            # Validate file existence
            if not os.path.exists(file_path):
                print(f"File not found: {file_path}\n")
                continue

            # Read and load the SQL script content
            with open(file_path, "r", encoding="utf-8") as f:
                sql_script = f.read()

            print(f"SQL content length: {len(sql_script)} characters")

            # Split SQL script into executable statements
            statements = [stmt.strip() for stmt in sql_script.split(";") if stmt.strip()]
            print(f"Found {len(statements)} statements to execute")

            for i, statement in enumerate(statements, 1):
                if statement.strip():
                    print(f"Executing statement {i}: {statement[:100]}...")
                    try:
                        cursor.execute(statement)
                        print(f"✓ Statement {i} executed successfully")
                    except Error as e:
                        print(f"✗ Error in statement {i}: {e}")
                        # Don't continue if table creation fails
                        raise

            print(f"Finished creating tables from {file_path}\n")

        # Commit changes
        conn.commit()
        print("All tables created successfully!\n")

    except Error as e:
        print(f"MySQL error: {e}\n")
        if conn:
            conn.rollback()

    finally:
        # Cleanup resources
        if cursor is not None:
            cursor.close()
            print("Cursor closed.\n")

        if conn is not None and conn.is_connected():
            conn.close()
            print("Connection closed.\n")