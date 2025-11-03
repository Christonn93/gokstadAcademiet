from database import connect_db
from mysql.connector import Error

"""
AI generated kode -> .docs/AI-Help/drop_database.md
"""

def drop_db(db_name: str, conn=None, cursor=None):
    """Remove (drop) the existing database and all its tables"""

    try:
        # Establish a connection to the MySQL server (not to a specific database)
        conn, cursor = connect_db()  # Make sure connect_db() connects without selecting a DB
        if not conn or not cursor:
            print("❌ Failed to connect to MySQL server. Cannot drop database.\n")
            return

        # Create a cursor object for executing SQL statements
        cursor = conn.cursor()

        # Write a SQL command to drop the database (use IF EXISTS to avoid crashing if it doesn't exist)
        sql = f"DROP DATABASE IF EXISTS {db_name}"

        # Execute the DROP DATABASE command
        cursor.execute(sql)

        # Commit the change to ensure the database is removed
        conn.commit()

        # Optionally print or return confirmation that the database was dropped
        print(f"✅ Database '{db_name}' has been dropped successfully.")

    except Error as e:
        # Handle potential MySQL errors (e.g., insufficient privileges, DB in use)
        print(f"❌ Error dropping database '{db_name}': {e}")

    finally:
        # Close the cursor and connection to clean up resources
        if cursor:
            cursor.close()
        if conn:
            conn.close()
