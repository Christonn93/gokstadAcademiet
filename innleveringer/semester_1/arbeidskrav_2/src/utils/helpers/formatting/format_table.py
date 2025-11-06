## AI help to produce this code: .docs/AI-Help/creating_reusable_formatter.md

def format_table(data):
    """Format query results (list of dicts) into a readable table."""

    # If no data, return a friendly message
    if not data:
        return "⚠️ No data found."

    # Extract headers dynamically from the first row
    headers = list(data[0].keys())

    # Calculate column widths (max of header width or longest value width)
    col_widths = {header: len(header) for header in headers}
    for row in data:
        for header in headers:
            col_widths[header] = max(col_widths[header], len(str(row.get(header, ""))))

    # Build table
    lines = []

    # Header row
    header_line = " | ".join(header.ljust(col_widths[header]) for header in headers)
    lines.append(header_line)
    lines.append("-" * len(header_line))

    # Data rows
    for row in data:
        line = " | ".join(str(row.get(header, "")).ljust(col_widths[header]) for header in headers)
        lines.append(line)

    return "\n".join(lines)
