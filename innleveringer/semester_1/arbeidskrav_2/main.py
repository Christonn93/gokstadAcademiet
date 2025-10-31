from constants.sql_files import sql_files
from database import test_connection, create_db, create_db_tables, seed_db
from utils import wait_for_enter as user_action

def main_program():
    """The main program"""

    # Test connection first and exit if it fails
    if not test_connection():
        return

    # Create database
    if sql_files["create_db"]:
        create_db([sql_files["create_db"]])
        user_action()

    # Create database tables
    if sql_files["create_tables"]:
        create_db_tables([sql_files["create_tables"]])
        user_action()

    # Seed data in to database tables
    if sql_files["seed_db"]:
        seed_db(sql_files["seed_db"])
        user_action()
    else:
        print("❌ Cannot seed data - tables are missing")

   # Start interface

if __name__ == '__main__':
    main_program()