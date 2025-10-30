def sum_extended(rows):
    total = 0
    for r in rows:
        total += r["Extended"]
    print("Total number of extension days:", total)
    return total

def main():
    rows = [
        {"Extended": 5},
        {"Extended": 3},
        {"Extended": 7}
    ]
    sum_extended(rows)

if __name__ == "__main__":
    main()