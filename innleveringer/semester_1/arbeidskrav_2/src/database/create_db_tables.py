import os
from mysql.connector import Error
from database.connect_db import connect_db


def create_db_tables(files: list[str] = None):
    """Create database tables from provided SQL files."""

    # Open database connection
    conn, cursor = connect_db()

    # Connection check
    if conn is None or cursor is None:
        print("❌ No database connection established.\n")
        return

    # SQL file check
    if not files:
        print("⚠️ No SQL files provided for creating tables.\n")
        cursor.close()
        conn.close()
        return

    try:
        for file_path in files:
            print(f"\n📄 Processing SQL file: {file_path}")

            if not os.path.exists(file_path):
                print(f"❌ File not found: {file_path}")
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                sql_script = f.read()

            print(f"📏 SQL file size: {len(sql_script)} characters")

            # Split into executable statements
            statements = [stmt.strip() for stmt in sql_script.split(";") if stmt.strip()]
            print(f"🛠 Found {len(statements)} SQL statements to execute.")

            # Execute each statement
            for i, statement in enumerate(statements, 1):
                print(f"➡ Executing statement {i}...")
                try:
                    cursor.execute(statement)
                    print(f"✅ Statement {i} executed successfully.")
                except Error as e:
                    print(f"❌ Error in statement {i}: {e}")
                    raise  # stop processing further files on failure

            print(f"✅ Finished executing file: {file_path}")

        conn.commit()
        print("\n🎉 All tables created successfully!\n")

    except Error as e:
        print(f"❌ MySQL error while creating tables: {e}")
        if conn:
            conn.rollback()

    finally:
        if cursor:
            cursor.close()
            print("🔒 Cursor closed.")
        if conn and conn.is_connected():
            conn.close()
            print("🔌 Connection closed.\n")
