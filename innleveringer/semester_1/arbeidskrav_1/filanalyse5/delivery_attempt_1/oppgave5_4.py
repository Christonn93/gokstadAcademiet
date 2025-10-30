def not_returned(rows):
    result = []
    for r in rows:
        if r["Returned"].lower() == "no":
            result.append((r["Book Title"], r["First Name"], r["Last Name"]))

    print("Books that were not returned:")
    for book, fn, ln in result:
        print(f"  {book} (borrowed by {fn} {ln})")
    return result

def main():
    rows = [
        {"Book Title": "Book A", "First Name": "John", "Last Name": "Doe", "Returned": "no"},
        {"Book Title": "Book B", "First Name": "Jane", "Last Name": "Smith", "Returned": "yes"},
        {"Book Title": "Book C", "First Name": "Alice", "Last Name": "Brown", "Returned": "no"}
    ]
    not_returned(rows)
