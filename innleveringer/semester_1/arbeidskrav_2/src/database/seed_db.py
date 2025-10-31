import os
from mysql.connector import Error
from src.database.connect_db import connect_db

def seed_db(file_path: str = None):
    """Populate the database with data from a SQL seed file"""

    # Using database connection
    conn, cursor = connect_db()

    # FIXED: Check if connection failed (conn or cursor is None)
    if conn is None or cursor is None:
        print("No database connection\n")
        return  # No need to close since connect_db already returned None, None

    # Check if file path was provided
    if not file_path:
        print("No SQL file provided for seeding.\n")
        cursor.close()
        conn.close()
        return

    print("\nStarting database seeding...\n")

    # Validate file path
    if not os.path.exists(file_path):
        print(f"SQL file not found: {file_path}")
        cursor.close()
        conn.close()
        return

    try:
        # Read SQL file content
        with open(file_path, "r", encoding="utf-8") as file:
            sql_script = file.read()

        # Split into individual SQL statements
        statements = [
            stmt.strip() for stmt in sql_script.split(";")
            if stmt.strip() and not stmt.strip().startswith("--")
        ]

        # Execute each statement one by one
        for statement in statements:
            try:
                cursor.execute(statement)
                print(f"✓ Executed: {statement[:60]}...")
            except Error as e:
                print(f"✗ Skipping statement due to error:\n{statement[:80]}...\n→ {e}")

        # Commit changes
        conn.commit()
        print("\nDatabase seeding completed successfully!\n")

    except Error as e:
        print(f"MySQL error during seeding: {e}")
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