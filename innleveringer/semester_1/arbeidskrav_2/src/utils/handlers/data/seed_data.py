from mysql.connector import Error


def seed_data(cursor, statements):
    """Execute a list of SQL statements and track results."""

    successful_statements = 0
    failed_statements = 0
    total = len(statements)

    for i, statement in enumerate(statements, 1):
        try:
            cursor.execute(statement)

            # Success log
            print(f"✅ SUCCESS [{i}/{total}] → {statement[:60]}...")

            if cursor.rowcount > 0:
                print(f"   ↳ Rows affected: {cursor.rowcount}")

            successful_statements += 1

        except Error as e:
            # Failure log
            print(f"❌ ERROR [{i}/{total}] → Skipped due to database error")
            print(f"   ↳ Statement: {statement[:80]}...")
            print(f"   ↳ Error: {e}")

            failed_statements += 1

    return successful_statements, failed_statements
