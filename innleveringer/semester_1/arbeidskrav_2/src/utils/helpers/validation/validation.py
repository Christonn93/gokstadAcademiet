from mysql.connector import Error
from datetime import datetime
import re
import os


class Validation:
    """A class for validating various data types and conditions."""

    @staticmethod
    def is_valid_seed_file(file_path: str):
        """Validate input parameters for seeding operation."""
        if not file_path:
            print("❌ ERROR: No SQL file provided for seeding.")
            return False

        if not os.path.exists(file_path):
            print(f"❌ ERROR: SQL file not found → {file_path}")
            return False

        if not os.path.isfile(file_path):
            print(f"❌ ERROR: Path is not a file → {file_path}")
            return False

        if not file_path.lower().endswith('.sql'):
            print(f"⚠️ WARNING: File does not have .sql extension → {file_path}")

        return True

    @staticmethod
    def is_valid_isbn(isbn):
        """Validate a 10- or 13-digit ISBN."""
        if not isinstance(isbn, str):
            return False

        isbn = isbn.replace("-", "").replace(" ", "").upper()

        if len(isbn) == 10 and isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X'):
            return True

        if len(isbn) == 13 and isbn.isdigit():
            return True

        return False

    @staticmethod
    def is_valid_date(date_str):
        """Validate a date string in YYYY-MM-DD format."""
        if not isinstance(date_str, str):
            return False

        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_borrower_id(borrower_id):
        """Validate a borrower ID (pattern: LNr followed by digits)."""
        if not isinstance(borrower_id, str):
            return False

        return re.match(r"^LNr\d+$", borrower_id) is not None

    @staticmethod
    def is_seed_valid(cursor):
        """Verify that data was inserted by counting records in key tables."""
        table_counts = {}

        try:
            tables_to_check = ['bok', 'låner', 'utlån']

            for table in tables_to_check:
                cursor.execute(f"SELECT COUNT(*) as count FROM {table}")
                result = cursor.fetchone()
                table_counts[table] = result[0] if result else 0

            print(
                f"✅ Data verification complete → "
                f"{table_counts['bok']} books, "
                f"{table_counts['låner']} members, "
                f"{table_counts['utlån']} loans in database."
            )

            return table_counts

        except Error as e:
            print(f"⚠️ WARNING: Could not verify data counts → {e}")
            return table_counts

    @staticmethod
    def is_connected(conn, cursor):
        """Validate that database connection is established."""
        if conn is None or cursor is None:
            print("❌ ERROR: No active database connection.")
            return False

        try:
            if hasattr(conn, "is_connected") and not conn.is_connected():
                print("❌ ERROR: Database connection is not active.")
                return False
        except Error as err:
            print(f"❌ ERROR: Could not verify connection status → {err}")
            return False

        return True
