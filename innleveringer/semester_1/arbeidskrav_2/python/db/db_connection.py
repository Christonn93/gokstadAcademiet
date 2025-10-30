import os
import mysql.connector
from mysql.connector import Error
from db_config import DB_CONFIG

# TODO: add code to docs
# Got some code setup from Marius that I extended upon (check readme)

def setup_database():
    conn = None
    cursor = None
    create_db_file = '../../sql/create_database.sql'
    file_encoding = 'utf-8'

    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        sql_path = os.path.join(os.path.dirname(__file__), create_db_file)
        with open(sql_path, 'r', encoding=file_encoding) as sql_file:
            sql_script = sql_file.read()

        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)

        conn.commit()
        print("Database opprettet!")

    except Error as e:
        print(f"\nConnection error: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()
        print("Tilkobling lukket.")


if __name__ == "__main__":
    setup_database()
