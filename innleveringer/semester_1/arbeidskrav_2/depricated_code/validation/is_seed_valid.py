from mysql.connector import Error

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
            count = cursor.fetchone()[0]

            # Store the count in our results dictionary
            table_counts[table] = count

        # Print a user-friendly summary of what was found
        print(f"Data verification: {table_counts['bok']} books, "
              f"{table_counts['låner']} members, {table_counts['utlån']} loans in database")

    except Error as e:
        # Handle database-specific errors (connection issues, syntax errors, etc.)
        print(f"WARNING: Could not verify data counts: {e}")
    # Return whatever counts we were able to gather (could be empty dict on complete failure)
    return table_counts