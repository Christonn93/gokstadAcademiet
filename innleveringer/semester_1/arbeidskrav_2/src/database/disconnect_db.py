def disconnect_db(cursor, conn):
    """Close database cursor and connection."""
    if cursor is not None:
        cursor.close()
        print("🔒 Cursor closed.")

    if conn is not None and conn.is_connected():
        conn.close()
        print("🔌 Database connection closed.")

    print("✅ Database resources cleaned up.\n")
