# Prompt:
Can you change my error, warning and success print with some descriptive icons ?

```python
import os
import time
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

from constants.sql_files import get_sql_files

# Load environment variables
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "database": os.getenv("DB_NAME"),
}

MAX_RETRIES = 3
RETRY_DELAY = 2


class DatabaseManager:
    def __init__(self, config: dict):
        self.config = config
        self.conn = None
        self.cursor = None

    # --- Helper to connect (with retry logic) ---
    def connect(self, use_database=True):
        """Connect to server or specific DB (if exists)."""
        config = self.config.copy()
        database_name = config.pop("database", None)
        attempts = 0

        while attempts < MAX_RETRIES:
            try:
                if use_database and database_name:
                    self.conn = mysql.connector.connect(**self.config)
                else:
                    self.conn = mysql.connector.connect(**config)

                self.cursor = self.conn.cursor()

                if use_database and database_name:
                    print(f"Connected to database '{database_name}'")
                else:
                    print("Connected to MySQL server (no database selected)")

                return True

            except Error as e:
                print(f"Connection error (attempt {attempts + 1}/{MAX_RETRIES}): {e}")
                attempts += 1
                time.sleep(RETRY_DELAY)

        return False

    # --- Clean disconnect ---
    def disconnect(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn and self.conn.is_connected():
                self.conn.close()
                print("🔌 Connection closed.")
        except Error as e:
            print(f"Error during disconnect: {e}")

    # --- Create database if it doesn't exist ---
    def create_database_if_not_exists(self):
        database_name = self.config.get("database")
        if not database_name:
            print("No database name provided in config.")
            return

        self.connect(use_database=False)
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database_name}`")
            print(f"Database '{database_name}' is ready.")
        except Error as e:
            print(f"Error creating database: {e}")
        finally:
            self.disconnect()

    # --- Drop full database ---
    def drop_database(self):
        database_name = self.config.get("database")
        self.connect(use_database=False)
        try:
            self.cursor.execute(f"DROP DATABASE IF EXISTS `{database_name}`")
            print(f"Database '{database_name}' has been dropped.")
        except Error as e:
            print(f"Error dropping database: {e}")
        finally:
            self.disconnect()

    # --- Execute SQL file (tables, seed, etc.) ---
    def execute_sql_file(self, file_path):
        if not os.path.exists(file_path):
            print(f"SQL file not found: {file_path}")
            return

        if not self.connect():
            print("Could not connect to database.")
            return

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                script = file.read()

            statements = [
                stmt.strip()
                for stmt in script.split(";")
                if stmt.strip() and not stmt.startswith("--")
            ]

            for stmt in statements:
                self.cursor.execute(stmt)

            self.conn.commit()
            print(f"Executed SQL file: {file_path}")

        except Error as e:
            print(f"SQL execution error: {e}")
            self.conn.rollback()
        finally:
            self.disconnect()

    # --- Simple reusable query function ---
    def query(self, sql, params=None, fetch=True):
        if not self.connect():
            return None

        try:
            self.cursor.execute(sql, params or ())
            if fetch:
                result = self.cursor.fetchall()
                return result
            else:
                self.conn.commit()
                return self.cursor.rowcount
        except Error as e:
            print(f"Query error: {e}")
        finally:
            self.disconnect()


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    files = get_sql_files()
    db = DatabaseManager(DB_CONFIG)

    # Option 1: Fully reset database each time (good during development)
    db.execute_sql_file(files["create_db"])
    db.execute_sql_file(files["create_tables"])
    db.execute_sql_file(files["seed_db"])
```

# Answer: 


Absolutely! Adding descriptive icons to your print statements can make the output more visually intuitive and easier to scan. Here's your updated code with icons added to `print` statements for **errors**, **warnings**, and **successes**:

### ✅ Icons Used:
- ❌ **Error** – for connection/query errors
- ⚠️ **Warning** – for warnings or non-critical issues
- ✅ **Success** – for successful operations
- 🔌 Already used for disconnect – kept as-is

---

### ✅ Updated Code Snippet (Only the print lines are changed):

```python
import os
import time
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

from constants.sql_files import get_sql_files

# Load environment variables
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "database": os.getenv("DB_NAME"),
}

MAX_RETRIES = 3
RETRY_DELAY = 2


class DatabaseManager:
    def __init__(self, config: dict):
        self.config = config
        self.conn = None
        self.cursor = None

    # --- Helper to connect (with retry logic) ---
    def connect(self, use_database=True):
        """Connect to server or specific DB (if exists)."""
        config = self.config.copy()
        database_name = config.pop("database", None)
        attempts = 0

        while attempts < MAX_RETRIES:
            try:
                if use_database and database_name:
                    self.conn = mysql.connector.connect(**self.config)
                else:
                    self.conn = mysql.connector.connect(**config)

                self.cursor = self.conn.cursor()

                if use_database and database_name:
                    print(f"✅ Connected to database '{database_name}'")
                else:
                    print("✅ Connected to MySQL server (no database selected)")

                return True

            except Error as e:
                print(f"❌ Connection error (attempt {attempts + 1}/{MAX_RETRIES}): {e}")
                attempts += 1
                time.sleep(RETRY_DELAY)

        return False

    # --- Clean disconnect ---
    def disconnect(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn and self.conn.is_connected():
                self.conn.close()
                print("🔌 Connection closed.")
        except Error as e:
            print(f"❌ Error during disconnect: {e}")

    # --- Create database if it doesn't exist ---
    def create_database_if_not_exists(self):
        database_name = self.config.get("database")
        if not database_name:
            print("⚠️ No database name provided in config.")
            return

        self.connect(use_database=False)
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database_name}`")
            print(f"✅ Database '{database_name}' is ready.")
        except Error as e:
            print(f"❌ Error creating database: {e}")
        finally:
            self.disconnect()

    # --- Drop full database ---
    def drop_database(self):
        database_name = self.config.get("database")
        self.connect(use_database=False)
        try:
            self.cursor.execute(f"DROP DATABASE IF EXISTS `{database_name}`")
            print(f"✅ Database '{database_name}' has been dropped.")
        except Error as e:
            print(f"❌ Error dropping database: {e}")
        finally:
            self.disconnect()

    # --- Execute SQL file (tables, seed, etc.) ---
    def execute_sql_file(self, file_path):
        if not os.path.exists(file_path):
            print(f"❌ SQL file not found: {file_path}")
            return

        if not self.connect():
            print("❌ Could not connect to database.")
            return

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                script = file.read()

            statements = [
                stmt.strip()
                for stmt in script.split(";")
                if stmt.strip() and not stmt.startswith("--")
            ]

            for stmt in statements:
                self.cursor.execute(stmt)

            self.conn.commit()
            print(f"✅ Executed SQL file: {file_path}")

        except Error as e:
            print(f"❌ SQL execution error: {e}")
            self.conn.rollback()
        finally:
            self.disconnect()

    # --- Simple reusable query function ---
    def query(self, sql, params=None, fetch=True):
        if not self.connect():
            return None

        try:
            self.cursor.execute(sql, params or ())
            if fetch:
                result = self.cursor.fetchall()
                return result
            else:
                self.conn.commit()
                return self.cursor.rowcount
        except Error as e:
            print(f"❌ Query error: {e}")
        finally:
            self.disconnect()


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    files = get_sql_files()
    db = DatabaseManager(DB_CONFIG)

    # Option 1: Fully reset database each time (good during development)
    db.execute_sql_file(files["create_db"])
    db.execute_sql_file(files["create_tables"])
    db.execute_sql_file(files["seed_db"])
```

---

### ✅ Summary of Icon Usage:
| Icon | Meaning    | Example Use                                   |
|------|------------|-----------------------------------------------|
| ✅    | Success    | Connection success, DB created, file executed |
| ❌    | Error      | Connection failure, SQL error, file not found |
| ⚠️   | Warning    | Missing database name                         |
| 🔌   | Disconnect | Already used for closing connection           |

Let me know if you'd like to add colors or emojis for richer output in terminal!