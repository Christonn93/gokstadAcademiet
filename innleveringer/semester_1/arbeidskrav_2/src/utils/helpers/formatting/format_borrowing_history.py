def format_borrowing_history(history):
    """Format borrowing history as a table string"""

    # Handle empty results
    if not history:
        return "No history found."

    # Define table headers and calculate initial column widths
    headers = ["Utlånsnr", "ISBN", "Utlånsdato", "Innlevert dato"]
    col_widths = {header: len(header) for header in headers}

    # Adjust column widths based on longest data per column
    for item in history:
        for header in headers:
            col_widths[header] = max(col_widths[header], len(str(item.get(header, ''))))

    # Build table as string
    lines = []

    # Table header
    header_line = " | ".join(header.ljust(col_widths[header]) for header in headers)
    lines.append(header_line)
    lines.append("-" * len(header_line))

    # Table rows
    for item in history:
        row_values = [
            str(item.get("Utlånsnr", '')).ljust(col_widths["Utlånsnr"]),
            str(item.get("ISBN", '')).ljust(col_widths["ISBN"]),
            str(item.get("Utlånsdato", '')).ljust(col_widths["Utlånsdato"]),
            str(item.get("Innlevert dato", '')).ljust(col_widths["Innlevert dato"])
        ]
        lines.append(" | ".join(row_values))

    return "\n".join(lines)