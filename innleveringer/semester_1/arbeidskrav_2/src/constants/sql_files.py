
import os
from constants.base import SQL_DIR

sql_files_dict = {
    "create_db": os.path.join(SQL_DIR, "create_database.sql"),
    "create_tables": os.path.join(SQL_DIR, "create_database_tables.sql"),
    "seed_db": os.path.join(SQL_DIR, "seed_database.sql"),
}
def sql_files():
    return sql_files_dict.copy()

__all__ = ['sql_files']