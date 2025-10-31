import os
from mysql.connector import connect, Error
from db_config import DB_CONFIG

def setup_database(files: list[str]):
    conn = None
    connect.HAVE_CEXT = False

    try:
        conn = connect(**DB_CONFIG)
        cursor = conn.cursor()

        print("✅ Connected to MySQL server.\n")

        for sql_file_name in files:
            print(f"\n📘 Running script [{sql_file_name}]...")

            # Verify file exists
            if not os.path.exists(sql_file_name):
                print(f"⚠️  File not found: {sql_file_name}\n")
                continue

            with open(sql_file_name, 'r', encoding='utf-8') as sql_file:
                sql_script = sql_file.read()

            # Execute all statements in file
            for statement in sql_script.split(';'):
                if statement.strip():
                    cursor.execute(statement)

            print(f"✅ Finished executing [{os.path.basename(sql_file_name)}]\n")

        conn.commit()
        print("\n🎉 Database setup completed successfully!")

    except Error as e:
        print(f"❌ MySQL error: {e}\n")
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("🔒 Connection closed.\n")


# Testing
if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    sql_files = [
        os.path.join(base_dir, "./sql/create_database.sql"),
        os.path.join(base_dir, "./sql/create_database_tables.sql"),
    ]
    setup_database(sql_files)