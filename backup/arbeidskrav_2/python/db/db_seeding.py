import os
from mysql.connector import connect, Error
from db_config import DB_CONFIG

def db_seeding(sql_file_path: str) -> None:
    """Populate the database with data from a SQL seed file"""
    conn = None
    cursor = None

    print("\n🌱 Starting database seeding...\n")

    if not os.path.exists(sql_file_path):
        print(f"❌ SQL file not found: {sql_file_path}")
        return

    try:
        # Connect to the MySQL database
        conn = connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Read and prepare SQL file content
        with open(sql_file_path, "r", encoding="utf-8") as file:
            sql_script = file.read()

        # Split into executable statements
        statements = [
            stmt.strip() for stmt in sql_script.split(";")
            if stmt.strip() and not stmt.strip().startswith("--")
        ]

        for statement in statements:
            try:
                cursor.execute(statement)
            except Error as e:
                print(f"⚠️  Skipping statement due to error:\n{statement[:80]}...\n→ {e}")

        conn.commit()
        print("\n✅ Database seeding completed successfully!\n")

    except Error as e:
        print(f"❌ MySQL error during seeding: {e}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("🔒 Connection closed.\n")
