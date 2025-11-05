from constants import sql_files
from database import connect_db, create_db, create_db_tables, seed_db
from utils.helpers import Validation


def database_service():
    # Get file paths for all SQL scripts needed for database setup
    sql_paths = sql_files()

    # Calling validation class
    validate = Validation()

    # Establish connection to the database
    conn, cursor = connect_db()

    # Verify database connection is working before proceeding
    if validate.is_connected(conn, cursor):
        pass  # Connection is valid, continue with setup

    # Create the database if it doesn't exist
    if sql_paths["create_db"]:
        create_db([sql_paths["create_db"]], conn, cursor)

    # Create all necessary tables in the database
    if sql_paths["create_tables"]:
        create_db_tables([sql_paths["create_tables"]])

    # Populate tables with initial data (seed data)
    if sql_paths["seed_db"]:
        seed_db(sql_paths["seed_db"])
    else:
        print("Cannot seed data - tables are missing")