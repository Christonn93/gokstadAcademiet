## Prompt: 

---

Currently, I have multiple table formatters. Can I have one that works no matter what ? 

```py
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


def format_books_table_tuples(books):
    if not books:
        return "No books found."

    headers = ["ISBN", "Tittel", "Forfatter", "Publikasjonsår"]
    col_widths = [len(h) for h in headers]

    for book in books:
        col_widths[0] = max(col_widths[0], len(str(book[0])))
        col_widths[1] = max(col_widths[1], len(str(book[1])))

    lines = []
    header_line = " | ".join(headers[i].ljust(col_widths[i]) for i in range(2))
    lines.append(header_line)
    lines.append("-" * len(header_line))

    for book in books:
        row = " | ".join(str(book[i]).ljust(col_widths[i]) for i in range(2))
        lines.append(row)

    return "\n".join(lines)
```

I want it to take all headers from what ever table I call for, not explicit tell the function about what the headers are. 


## Answer: 

---

Yes — you can absolutely have **one table formatter function** that works for *any* query, *any* table, and *any* set of columns — without hardcoding headers like `"ISBN"` or `"Tittel"` or `"Utlånsnr"`.

Right now your formatters are:

* Repeating lots of similar logic
* Locked to specific column names
* Some only work for tuples, others only for dictionaries

---

### ✅ The Goal

Create one function:

✔ Works with dictionary results (`cursor = conn.cursor(dictionary=True)`)
✔ Automatically uses whatever column names the query returns
✔ Dynamically adjusts column widths
✔ Works for any table or join
✔ No hardcoded headers

---

### ✅ Universal Table Formatter (Drop-In Solution)

```python
def format_table(data):
    """Format query results (list of dicts) into a readable table."""

    # If no data, return a friendly message
    if not data:
        return "No data found."

    # Extract headers dynamically from the first row
    headers = list(data[0].keys())

    # Calculate column widths (header vs. cell values)
    col_widths = {header: len(header) for header in headers}
    for row in data:
        for header in headers:
            col_widths[header] = max(col_widths[header], len(str(row.get(header, ""))))

    # Build formatted table
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
```

---

### ✅ ✅ Usage Example

Assume your query returns:

```python
result = query_db("SELECT Forfatter, Tittel FROM bok ORDER BY Forfatter ASC")
print(format_table(result))
```

You get:

```
Forfatter            | Tittel
--------------------+-------------------------
Bjørneboe, Jens     | Jonas
Hamsun, Knut        | Victoria
Hemingway, Ernest   | Den gamle mannen og havet
...
```

Same function works for loans:

```python
result = query_db("""
    SELECT u.UtlånsNr, l.Fornavn, l.Etternavn, b.Tittel, u.Utlånsdato
    FROM utlån AS u
    JOIN låner AS l ON u.LNr = l.LNr
    JOIN bok AS b ON u.ISBN = b.ISBN
""")
print(format_table(result))
```

Same function works for copies, borrowers, even joins — no changes needed.

---

### ✅ Important Requirement

This only works if your `query_db()` returns **list of dictionaries**, not tuples.

So make sure inside `query_db()` you have:

```python
cursor = conn.cursor(dictionary=True)
```

---

### ✅ What You Can Delete Now

You **no longer need:**

* `format_books_table()`
* `format_books_table_tuples()`
* `format_borrowing_history()`
* Any specialized table formatting

**Just use `format_table(data)` for everything.**

---

### ✅ Want Borders, Center Alignment or Colors Later?

That can be added on top — but only *after* this universal formatter is in place.

---
