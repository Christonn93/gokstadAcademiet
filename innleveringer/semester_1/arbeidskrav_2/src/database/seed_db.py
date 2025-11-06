from mysql.connector import Error

from database import connect_db
from database.disconnect_db import disconnect_db
from utils.handlers.data.seed_data import seed_data
from utils.handlers.parser.parse_sql_file import parse_sql_file
from utils.helpers import Validation


def seed_db(file_path: str = None):
    """Main function to populate the database with data from a SQL seed file."""

    print("\n🌱 Starting database seeding process...")

    validate = Validation()

    # Validate seed file path
    if not validate.is_valid_seed_file(file_path):
        print("❌ Invalid or missing SQL seed file.")
        return

    # Establish database connection
    conn, cursor = connect_db()
    if not validate.is_connected(conn, cursor):
        print("❌ Database connection failed — seeding aborted.")
        return

    print("✅ Database connection established.")
    print(f"📂 Seed file: {file_path}\n")

    try:
        # Parse SQL statements from file
        statements = parse_sql_file(file_path)

        if not statements:
            print("⚠️ No valid SQL statements found in the seed file.")
            return

        print(f"🛠 Executing {len(statements)} SQL statements...")

        successful_statements, failed_statements = seed_data(cursor, statements)
        conn.commit()

        print("\n✅ Database seeding completed.")
        print(f"📊 Summary: {successful_statements} succeeded, {failed_statements} failed")

        # Optional data verification logic
        if successful_statements > 0:
            print("💾 Changes committed to the database.")
            validate.is_seed_valid(cursor)
        else:
            print("⚠️ No statements were successfully executed.")

    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")

    except Error as e:
        print(f"❌ MySQL error during seeding: {e}")
        if conn:
            conn.rollback()
            print("↩️ All changes rolled back due to MySQL error.")

    except Exception as e:
        print(f"❌ Unexpected error during seeding: {e}")
        if conn:
            conn.rollback()
            print("↩️ All changes rolled back due to unexpected error.")

    finally:
        disconnect_db(cursor, conn)
