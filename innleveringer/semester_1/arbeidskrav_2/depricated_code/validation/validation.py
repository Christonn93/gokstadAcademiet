from mysql.connector import Error
from datetime import datetime
import re
import os


class Validation:
    """A class for validating various data types and conditions"""

    @staticmethod
    def is_valid_seed_file(file_path: str):
        """Validate input parameters for seeding operation"""
        if not file_path:
            print("ERROR: No SQL file provided for seeding.")
            return False

        if not os.path.exists(file_path):
            print(f"ERROR: SQL file not found: {file_path}")
            return False

        # Check if it's actually a file (not a directory)
        if not os.path.isfile(file_path):
            print(f"ERROR: Path is not a file: {file_path}")
            return False

        # Check file extension
        if not file_path.lower().endswith('.sql'):
            print(f"WARNING: File does not have .sql extension: {file_path}")

        return True

    @staticmethod
    def is_valid_isbn(isbn):
        """Validate a 10- or 13-digit ISBN"""

        # Check if input is string
        if not isinstance(isbn, str):
            return False

        # Remove hyphens and spaces, convert to uppercase for consistency
        isbn = isbn.replace("-", "").replace(" ", "").upper()

        # Validate ISBN-10 format (last digit may be 'X')
        if len(isbn) == 10 and isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X'):
            return True

        # Validate ISBN-13 format (all digits)
        if len(isbn) == 13 and isbn.isdigit():
            return True

        # Return False if neither format matches
        return False

    @staticmethod
    def is_valid_date(date_str):
        """Validate a date string in YYYY-MM-DD format"""

        # Check if input is string
        if not isinstance(date_str, str):
            return False

        # Attempt to parse the date using datetime; catch invalid formats
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_borrower_id(borrower_id):
        """Validate a borrower ID (pattern: LNr followed by digits)"""

        # Check if input is string
        if not isinstance(borrower_id, str):
            return False

        # Check borrower ID format with a regular expression
        return re.match(r"^LNr\d+$", borrower_id) is not None

    @staticmethod
    def is_seed_valid(cursor):
        """Verify that data was inserted by counting records in key tables"""

        # Dictionary to store counts for each table we check
        table_counts = {}

        try:
            # Define the core tables that should contain data after seeding
            tables_to_check = ['bok', 'låner', 'utlån']

            # Check each table sequentially
            for table in tables_to_check:
                # Execute count query for the current table
                cursor.execute(f"SELECT COUNT(*) as count FROM {table}")

                # Fetch the result - returns a tuple where first element is the count
                result = cursor.fetchone()
                count = result[0] if result else 0

                # Store the count in our results dictionary
                table_counts[table] = count

            # Print a user-friendly summary of what was found
            print(f"Data verification: {table_counts['bok']} books, "
                  f"{table_counts['låner']} members, {table_counts['utlån']} loans in database")

            return table_counts

        except Error as e:
            # Handle database-specific errors (connection issues, syntax errors, etc.)
            print(f"WARNING: Could not verify data counts: {e}")
            return table_counts

    @staticmethod
    def is_connected(conn, cursor):
        """Validate that database connection is established"""
        if conn is None or cursor is None:
            print("ERROR: No database connection available")
            return False

        # Additional check to verify the connection is actually active
        try:
            if hasattr(conn, 'is_connected') and not conn.is_connected():
                print("ERROR: Database connection is not active")
                return False
        except Error as err:
            print(f"ERROR: Could not verify connection status: {err}")
            return False

        return True

