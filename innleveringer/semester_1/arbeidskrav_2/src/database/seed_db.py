from mysql.connector import Error

from database import connect_db
from database.disconnect_db import disconnect_db
from utils.handlers.data.seed_data import seed_data
from utils.handlers.parser.parse_sql_file import parse_sql_file
from utils.helpers import Validation


def seed_db(file_path: str = None):
    """Main function to populate the database with data from a SQL seed file"""

    print("Starting database seeding function...")

    # Calling validation
    validate = Validation()

    # Validate input parameters
    if not validate.is_valid_seed_file(file_path):
        return

    # Establish database connection
    conn, cursor = connect_db()

    if not validate.is_connected(conn, cursor):
        return

    print("SUCCESS: Database connection established")
    print(f"SQL file path: {file_path}")
    print("\nStarting database seeding process...\n")

    try:
        # Parse SQL file into executable statements
        statements = parse_sql_file(file_path)

        if not statements:
            print("WARNING: No executable SQL statements found in file")
            return

        # Execute all SQL statements
        successful_statements, failed_statements = seed_data(cursor, statements)

        # Commit changes to database
        conn.commit()
        print(f"\nDatabase seeding completed!")
        print(f"Summary: {successful_statements} successful, {failed_statements} failed")

        # Verify data was inserted (only if we had successful statements)
        if successful_statements > 0:
            print("Changes committed to database")
            validate.is_seed_valid(cursor)
        else:
            print("WARNING: No successful statements executed")

    except FileNotFoundError as e:
        print(f"ERROR: {e}")

    except Error as e:
        print(f"MySQL error during seeding: {e}")
        if conn:
            conn.rollback()
            print("All changes rolled back due to error")
    except Exception as e:
        print(f"Unexpected error during seeding: {e}")
        if conn:
            conn.rollback()
            print("All changes rolled back due to unexpected error")
    finally:
        # Always clean up resources
        disconnect_db(cursor, conn)