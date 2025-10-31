from database.connect_db import connect_db
from utils.handlers.error.handle_connection_error import handle_connection_error

def test_connection():
    """Test database connection and return status"""
    print("Testing database connection...")
    conn, cursor = connect_db()

    if conn is None or cursor is None:
        handle_connection_error()
        return False

    # Close the test connection
    cursor.close()
    conn.close()
    print("✅ Database connection successful!\n")
    return True