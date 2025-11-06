from mysql.connector import connect, Error
from config import DB_CONFIG


def connect_db():
    """Establish and return a database connection with a cursor"""
    conn = None
    cursor = None

    try:
        # Copy config and extract database name
        config = DB_CONFIG.copy()
        database_name = config.pop('database', None)

        if not database_name:
            print("❌ No database name specified in configuration.")
            return None, None

        # Connect to MySQL server (without selecting database yet)
        conn = connect(**config)
        cursor = conn.cursor()
        print("✅ Connected to MySQL server.")

        # Check if database exists
        cursor.execute("SHOW DATABASES LIKE %s", (database_name,))
        database_exists = cursor.fetchone() is not None

        if database_exists:
            print(f"📁 Database '{database_name}' exists. Reconnecting using it...")
            # Reconnect WITH the database selected
            cursor.close()
            conn.close()
            conn = connect(**DB_CONFIG)
            cursor = conn.cursor()
            print(f"✅ Now using database: '{database_name}'.")
        else:
            print(f"⚠️ Database '{database_name}' does not exist. Connected only to server.")

        return conn, cursor

    except Error as e:
        print(f"❌ MySQL connection error: {e}")
        return None, None
