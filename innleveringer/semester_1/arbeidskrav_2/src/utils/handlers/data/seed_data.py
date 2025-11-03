from mysql.connector import Error


def seed_data(cursor, statements):
    """Execute a list of SQL statements and track results"""

    # Initialize counters to track execution results
    successful_statements = 0
    failed_statements = 0

    # Iterate through each statement with index starting at 1 for user-friendly numbering
    for i, statement in enumerate(statements, 1):
        try:
            # Attempt to execute the current SQL statement
            cursor.execute(statement)

            # Log successful execution with progress indicator [current/total]
            print(f"SUCCESS [{i}/{len(statements)}] Executed: {statement[:60]}...")

            # Increment success counter
            successful_statements += 1

            # Check if the statement affected any rows (INSERT, UPDATE, DELETE operations)
            if cursor.rowcount > 0:
                # Show impact of the operation
                print(f"   Rows affected: {cursor.rowcount}")

        except Error as e:
            # Handle database errors gracefully without stopping the entire process
            print(f"ERROR [{i}/{len(statements)}] Skipping statement due to error:")

            # Show truncated statement for context
            print(f"   Statement: {statement[:80]}...")

            # Display the actual error message
            print(f"   Error details: {e}")

            # Increment failure counter
            failed_statements += 1

    # Return both counters so caller knows the overall execution outcome
    return successful_statements, failed_statements