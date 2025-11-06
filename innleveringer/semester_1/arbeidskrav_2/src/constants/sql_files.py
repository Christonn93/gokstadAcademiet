import os
from constants.base import SQL_DIR

# ---------------------------------
#  SQL file paths in one place
# ---------------------------------
SQL_FILES = {
    "create_db": os.path.join(SQL_DIR, "create_database.sql"),
    "create_tables": os.path.join(SQL_DIR, "create_database_tables.sql"),
    "seed_db": os.path.join(SQL_DIR, "seed_database.sql"),
}

def get_sql_files():
    """Return a copy of SQL file paths dict."""
    return SQL_FILES.copy()

__all__ = ["get_sql_files"]