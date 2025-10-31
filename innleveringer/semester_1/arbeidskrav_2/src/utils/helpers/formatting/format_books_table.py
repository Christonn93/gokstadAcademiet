def format_books_table(books):
    """Format books data as a table string"""

    # Handle empty results
    if not books:
        return "No books found."

    # Define table headers and calculate initial column widths
    headers = ["ISBN", "Tittel", "Forfatter", "Publikasjonsår"]
    col_widths = {header: len(header) for header in headers}

    # Adjust column widths based on the longest data in each column
    for book in books:
        for header in headers:
            col_widths[header] = max(col_widths[header], len(str(book.get(header, ''))))

    # Build table as string
    lines = []

    # Table header
    header_line = " | ".join(header.ljust(col_widths[header]) for header in headers)
    lines.append(header_line)
    lines.append("-" * len(header_line))

    # Table rows
    for book in books:
        row_values = [
            str(book.get("ISBN", '')).ljust(col_widths["ISBN"]),
            str(book.get("Tittel", '')).ljust(col_widths["Tittel"]),
            str(book.get("Forfatter", '')).ljust(col_widths["Forfatter"]),
            str(book.get("Publikasjonsår", '')).ljust(col_widths["Publikasjonsår"])
        ]
        lines.append(" | ".join(row_values))

    return "\n".join(lines)