def handle_connection_error():
    print("\n❌ CRITICAL: Failed to connect to database.")
    print("🔍 Please check the following:")
    print("   1️⃣  Is the MySQL server running?")
    print("   2️⃣  If using Docker → run:  docker ps   (to check containers)")
    print("   3️⃣  Is DB_CONFIG correctly set in src/config/database.py?")
    print("   4️⃣  Verify host, port, username, and password are correct.\n")
    return
