from db.db_connection import Database
from db.run_sql import run_sql_file
import os

def create_database():
    """Creates the database using SQL file execution."""
    try:
        sql_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../sql/create_database.sql"))
        run_sql_file(sql_path)
        print("✅ Database created successfully.")
        return True
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        return False


def create_database_tables():
    pass

def seed_database_table():
    pass
