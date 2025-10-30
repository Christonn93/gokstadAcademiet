def count_by_genre(rows):
    counts = {}
    for r in rows:
        genre = r["Genre"]
        if genre not in counts:
            counts[genre] = 0
        counts[genre] += 1

    print("Number of books per genre:")
    for g in counts:
        print(f"  {g}: {counts[g]}")
    return counts

def main():
    rows = [
        {"Genre": "Fiction"},
        {"Genre": "Non-Fiction"},
        {"Genre": "Fiction"}
    ]
    count_by_genre(rows)

if __name__ == "__main__":
    main()