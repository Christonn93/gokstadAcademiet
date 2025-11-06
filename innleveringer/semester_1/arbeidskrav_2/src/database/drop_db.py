from database import connect_db
from mysql.connector import Error

"""
AI generated kode -> .docs/AI-Help/drop_database.md
"""

def drop_db(db_name: str, conn=None, cursor=None):
    """Remove the existing database and all its tables."""

    try:
        # Connect to MySQL server (not selecting a specific database)
        conn, cursor = connect_db()
        if not conn or not cursor:
            print("❌ Could not connect to MySQL server — database drop aborted.\n")
            return

        # Prepare and execute DROP DATABASE statement
        sql = f"DROP DATABASE IF EXISTS {db_name}"
        cursor.execute(sql)
        conn.commit()

        print(f"⚠️  Database '{db_name}' has been dropped successfully.")

    except Error as e:
        print(f"❌ Failed to drop database '{db_name}': {e}")

    finally:
        if cursor:
            cursor.close()
            print("🔒 Cursor closed.")
        if conn and conn.is_connected():
            conn.close()
            print("🔌 Connection closed.\n")
