
Since this is not part of the assignment, I have asked AI to produce this code, so I can complete the loop.

## Prompt: 

---

Create a drop db function. 

```python
def drop_db(conn=None, cursor=None,):
    """Remove (drop) the existing database and all its tables"""

    # Establish a connection to the MySQL server (not the specific database)

    # Create a cursor object for executing SQL statements

    # Write a SQL command to drop the database (e.g., "DROP DATABASE db_name")

    # Execute the DROP DATABASE command

    # Commit the change to ensure the database is removed

    # Handle potential MySQL errors (e.g., database does not exist)

    # Close the cursor and connection to clean up resources

    # Optionally print or return confirmation that the database was dropped


    try:
        # Establish a database connection (reuse an existing connection or create a new one)
        conn, cursor = connect_db()
        if conn is None or cursor is None:
            print("Failed to establish database connection. Cannot create database.\n")
            return None

        cursor = conn.cursor(dictionary=True)
```

## Answer: 

---


Here's a clean and complete **`drop_db()`** function that does exactly what your comments describe:
it connects to MySQL (not a specific database), drops the database safely, handles errors, and cleans up.

I kept your comment structure and filled in the logic.

---

### ✅ **Complete `drop_db()` Function (With Comments Kept)**

```python
from database import connect_db  # Reuse your existing connection function
import mysql.connector
from mysql.connector import Error

def drop_db(db_name: str, conn=None, cursor=None):
    """Remove (drop) the existing database and all its tables"""

    try:
        # Establish a connection to the MySQL server (not to a specific database)
        conn, cursor = connect_db()  # Make sure connect_db() connects without selecting a DB
        if not conn or not cursor:
            print("❌ Failed to connect to MySQL server. Cannot drop database.\n")
            return

        # Create a cursor object for executing SQL statements
        cursor = conn.cursor()

        # Write a SQL command to drop the database (use IF EXISTS to avoid crashing if it doesn't exist)
        sql = f"DROP DATABASE IF EXISTS {db_name}"

        # Execute the DROP DATABASE command
        cursor.execute(sql)

        # Commit the change to ensure the database is removed
        conn.commit()

        # Optionally print or return confirmation that the database was dropped
        print(f"✅ Database '{db_name}' has been dropped successfully.")

    except Error as e:
        # Handle potential MySQL errors (e.g., insufficient privileges, DB in use)
        print(f"❌ Error dropping database '{db_name}': {e}")

    finally:
        # Close the cursor and connection to clean up resources
        if cursor:
            cursor.close()
        if conn:
            conn.close()
```

---

### ✅ **How to Use It**

```python
drop_db("ga_bibliotek")  # Example – drops your library database
```

---

### ⚠️ **Important Reminders**

✔ This deletes **everything inside the database — all tables and data.**
✔ Use this only when you're sure you want to reset or remove the database.
✔ Your `connect_db()` must connect to MySQL **without auto-selecting a database**, or else MySQL might block the drop.

---

### ✅ Optional Upgrade: Confirm Before Dropping

Want safety?

```python
confirm = input(f"Are you sure you want to delete database '{db_name}'? (yes/no): ")
if confirm.lower() == "yes":
    drop_db(db_name)
```

---
