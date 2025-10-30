import os
import mysql.connector
from db_config import DB_CONFIG

def run_sql_file(file_path):
    # Prepare connection config without database
    base_config = DB_CONFIG.copy()
    base_config.pop("database", None)

    connection = mysql.connector.connect(**base_config)
    cursor = connection.cursor()

    with open(file_path, "r", encoding="utf-8") as f:
        sql_script = f.read()

    for statement in sql_script.split(';'):
        stmt = statement.strip()
        if stmt:
            try:
                cursor.execute(stmt)
            except mysql.connector.Error as err:
                print(f"⚠️ Error executing '{stmt[:40]}...': {err}")

    connection.commit()
    cursor.close()
    connection.close()
    print("✅ SQL file executed successfully!")

if __name__ == "__main__":
    sql_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../sql/create_database.sql"))
    run_sql_file(sql_path)
