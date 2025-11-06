from constants import get_sql_files
from database import connect_db, create_db, create_db_tables, seed_db
from utils.helpers import Validation


def database_service():
    """Run full database setup: create DB, create tables, seed data."""

    print("\n🚀 Starting database setup service...")

    sql_paths = get_sql_files()
    validate = Validation()

    # Establish initial database connection
    conn, cursor = connect_db()
    if not validate.is_connected(conn, cursor):
        print("❌ Database connection failed — stopping service.\n")
        return

    print("✅ Database connection confirmed.\n")

    # 1. Create the database
    if sql_paths.get("create_db"):
        print(f"📂 Creating database using: {sql_paths['create_db']}")
        create_db([sql_paths["create_db"]], conn, cursor)
    else:
        print("⚠️ No create_db file found — skipping database creation.")

    # 2. Create tables
    if sql_paths.get("create_tables"):
        print(f"🛠 Creating tables from: {sql_paths['create_tables']}")
        create_db_tables([sql_paths["create_tables"]])
    else:
        print("⚠️ No create_tables file found — skipping table creation.")

    # 3. Insert seed data
    if sql_paths.get("seed_db"):
        print(f"🌱 Seeding database with: {sql_paths['seed_db']}")
        seed_db(sql_paths["seed_db"])
    else:
        print("⚠️ Cannot seed data — seed SQL file is missing.")

    print("\n✅ Database service completed successfully.\n")
