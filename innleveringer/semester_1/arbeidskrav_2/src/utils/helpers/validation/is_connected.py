def is_connected(conn, cursor):
    """Validate that database connection is established"""
    if conn is None or cursor is None:
        print("ERROR: No database connection available")
        return False
    return True