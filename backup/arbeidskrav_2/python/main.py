import os
from db import setup_database

# Setting global variables
base_dir = os.path.dirname(__file__)

def create_db():
    print("Creating database\n")
    sql_files = [
        os.path.join(base_dir, "./sql/create_database.sql"),
        os.path.join(base_dir, "./sql/create_database_tables.sql"),
    ]
    setup_database(sql_files)

def seed_db():
    print("Seed database\n")
    seed_file = os.path.join(base_dir, "./sql/seed_data.sql")
    # db_seeding(seed_file)


def main():
    """Starting the program setup"""
    # Database connection
    create_db()

    # Seed database
    # seed_db()


    # Run interface

if __name__ == "__main__":
    main()
