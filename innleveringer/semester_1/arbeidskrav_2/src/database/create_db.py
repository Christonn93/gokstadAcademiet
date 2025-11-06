import os
from mysql.connector import Error


def create_db(files: list[str], conn, cursor):
    """Execute SQL files to create database + tables."""

    if not files:
        print("⚠️  No SQL files provided for database creation.")
        return

    if not conn or not cursor:
        print("❌ No active database connection — aborting.")
        return

    try:
        for filename in files:
            print(f"\n📂 Opening file: {filename}")

            if not os.path.exists(filename):
                print(f"❌ File does not exist: {filename}")
                continue

            with open(filename, "r", encoding="utf-8") as file:
                sql_script = file.read()

            statements = [stmt.strip() for stmt in sql_script.split(";") if stmt.strip()]

            print(f"⚙️  Executing {len(statements)} SQL statements...")
            for stmt in statements:
                cursor.execute(stmt)

            print(f"✅ Finished executing: {filename}")

        conn.commit()
        print("\n🎉 Database created and initialized successfully!\n")

    except Error as e:
        print(f"❌ MySQL Error during create_db: {e}")
        conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()