def print_books_table(books):
    if not books:
        print("No books found.")
        return

    # Determine column widths
    headers = ["ISBN", "Tittel", "Forfatter", "Publikasjonsår"]
    col_widths = {header: len(header) for header in headers}

    for book in books:
        for header in headers:
            col_widths[header] = max(col_widths[header], len(str(book.get(header, ''))))

    # Print header
    header_line = " | ".join(header.ljust(col_widths[header]) for header in headers)
    print(header_line)
    print("-" * len(header_line))

    # Print rows
    for book in books:
        row_values = [
            str(book.get("ISBN", '')).ljust(col_widths["ISBN"]),
            str(book.get("Tittel", '')).ljust(col_widths["Tittel"]),
            str(book.get("Forfatter", '')).ljust(col_widths["Forfatter"]),
            str(book.get("Publikasjonsår", '')).ljust(col_widths["Publikasjonsår"])
        ]
        print(" | ".join(row_values))

def print_history(history):
    if not history:
        print("No history found.")
        return

    headers = ["Utlånsnr", "ISBN", "Utlånsdato", "Innlevert dato"]
    col_widths = {header: len(header) for header in headers}

    for item in history:
        for header in headers:
            col_widths[header] = max(col_widths[header], len(str(item.get(header, ''))))

    # Print header
    header_line = " | ".join(header.ljust(col_widths[header]) for header in headers)
    print(header_line)
    print("-" * len(header_line))

    # Print rows
    for item in history:
        row_values = [
            str(item.get("Utlånsnr", '')).ljust(col_widths["Utlånsnr"]),
            str(item.get("ISBN", '')).ljust(col_widths["ISBN"]),
            str(item.get("Utlånsdato", '')).ljust(col_widths["Utlånsdato"]),
            str(item.get("Innlevert dato", '')).ljust(col_widths["Innlevert dato"])
        ]
        print(" | ".join(row_values))