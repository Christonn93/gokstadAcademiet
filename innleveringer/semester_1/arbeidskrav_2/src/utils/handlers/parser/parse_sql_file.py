import os

def parse_sql_file(file_path: str):
    """Parse SQL file and extract executable statements."""

    # Validate that file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ SQL file not found: {file_path}")

    # Read SQL content
    with open(file_path, "r", encoding="utf-8") as file:
        sql_script = file.read()

    print(f"📄 Loaded SQL file: '{file_path}' ({len(sql_script)} characters)")

    statements = []
    current_statement = ""
    in_multiline_comment = False

    for line in sql_script.split('\n'):
        stripped_line = line.strip()

        if not stripped_line:
            continue

        # Handle /* ... */ block comments
        if stripped_line.startswith('/*'):
            in_multiline_comment = True
            continue
        if in_multiline_comment and '*/' in stripped_line:
            in_multiline_comment = False
            remaining = stripped_line.split('*/', 1)[1].strip()
            if remaining:
                current_statement += remaining + " "
            continue
        if in_multiline_comment:
            continue

        # Skip single-line comments
        if stripped_line.startswith('--'):
            continue

        # Add valid SQL line
        current_statement += line + " "

        if ';' in line:
            parts = current_statement.split(';', 1)
            complete_statement = parts[0].strip()
            if complete_statement:
                statements.append(complete_statement)

            current_statement = parts[1] if len(parts) > 1 else ""

    # If last statement has no semicolon
    if current_statement.strip():
        statements.append(current_statement.strip())

    print(f"✅ Parsed {len(statements)} SQL statements.")
    return statements
