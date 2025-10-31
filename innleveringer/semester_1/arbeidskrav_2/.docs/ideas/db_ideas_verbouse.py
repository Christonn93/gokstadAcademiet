from mysql.connector import connect, Error

from src.config.database import DB_CONFIG


def connect_db(verbose=True):
    """Establish and return a database connection with a cursor"""
    conn = None
    cursor = None

    try:
        # Connect to MySQL server WITHOUT specifying database
        config = DB_CONFIG.copy()
        database_name = config.pop('database', None)

        if not database_name:
            if verbose:
                print("No database name specified in configuration")
            return None, None

        # Connect to MySQL server (not specific database)
        conn = connect(**config)
        cursor = conn.cursor()
        if verbose:
            print(f"✅ Connected to MySQL server")

        # Check if database exists
        cursor.execute("SHOW DATABASES LIKE %s", (database_name,))
        database_exists = cursor.fetchone() is not None

        if database_exists:
            if verbose:
                print(f"✅ Database '{database_name}' exists")
            # Close and reconnect WITH the database
            cursor.close()
            conn.close()
            conn = connect(**DB_CONFIG)
            cursor = conn.cursor()
            if verbose:
                print(f"✅ Now using database: {database_name}")
        else:
            if verbose:
                print(f"📝 Database '{database_name}' does not exist")
            # Keep connection without database - it will be created later

        return conn, cursor

    except Error as e:
        if verbose:
            print(f"MySQL connection error: {e}\n")
        return None, None