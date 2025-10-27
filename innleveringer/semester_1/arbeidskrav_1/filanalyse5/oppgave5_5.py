def most_borrowed(rows):
    counts = {}
    for r in rows:
        book = r["Book_title"]
        if book not in counts:
            counts[book] = 0
        counts[book] += 1

    max_count = max(counts.values()) if counts else 0
    most = [b for b in counts if counts[b] == max_count]

    most.sort()

    print("Most borrowed books:")
    for b in most:
        print(f"  {b}: {counts[b]}")
    return {b: counts[b] for b in most}

def main():
    rows = [
        {"Book_title": "Book A"},
        {"Book_title": "Book B"},
        {"Book_title": "Book A"}
    ]
    most_borrowed(rows)

if __name__ == "__main__":
    main()