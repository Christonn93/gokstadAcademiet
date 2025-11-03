def handle_connection_error():
    print("CRITICAL: Cannot connect to database.")
    print("Please check:")
    print("1. Is MySQL server running?")
    print("2. If using Docker: run 'docker ps' to check containers")
    print("3. Check your DB_CONFIG in src/config/database.py")
    print("4. Verify host, port, username, and password are correct")
    return