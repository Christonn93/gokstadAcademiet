import os

def parse_sql_file(file_path: str):
    """Parse SQL file and extract executable statements"""

    # Check if the SQL file exists before attempting to read it
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"SQL file not found: {file_path}")

    # Read the entire SQL file content with UTF-8 encoding to handle special characters
    with open(file_path, "r", encoding="utf-8") as file:
        sql_script = file.read()

    print(f"Read SQL file ({len(sql_script)} characters)")

    # Initialize variables for parsing
    # Will store the final executable SQL statements
    statements = []

    # Accumulates lines for the current statement being built
    current_statement = ""

    # Tracks whether we're inside a /* */ comment block
    in_multiline_comment = False

    # Process each line in the SQL file
    for line in sql_script.split('\n'):
        stripped_line = line.strip()

        # Skip empty lines to avoid unnecessary processing
        if not stripped_line:
            continue

        # Handle multi-line comments (/* ... */)
        if stripped_line.startswith('/*'):
            in_multiline_comment = True  # Entered a comment block
            continue  # Skip this line entirely
        if in_multiline_comment and '*/' in stripped_line:
            in_multiline_comment = False  # Exited the comment block
            # Extract any SQL code that comes after the closing comment marker
            remaining = stripped_line.split('*/', 1)[1].strip()
            if remaining:
                current_statement += remaining + " "
            continue  # Move to next line
        if in_multiline_comment:
            continue  # Still inside comment block, skip this line

        # Skip single-line comments (-- ...)
        if stripped_line.startswith('--'):
            continue  # Ignore comment lines

        # Add the current line to the statement being built
        current_statement += line + " "

        # Check if we've reached the end of a SQL statement (semicolon)
        if ';' in line:
            # Split on the first semicolon to separate the completed statement
            parts = current_statement.split(';', 1)
            complete_statement = parts[0].strip()

            # Only add non-empty statements to our list
            if complete_statement:
                statements.append(complete_statement)

            # Keep any content after the semicolon for the next statement
            current_statement = parts[1] if len(parts) > 1 else ""

    # Handle any SQL content that didn't end with a semicolon
    if current_statement.strip():
        statements.append(current_statement.strip())

    print(f"Found {len(statements)} SQL statements to execute")
    return statements