FILENAME = "bookloan.csv"

def read_data(filename=FILENAME):
    rows = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    headers = lines[0].strip().split(",")

    for line in lines[1:]:
        parts = line.strip().split(",")

        if len(parts) != len(headers):
            continue

        row = dict(zip(headers, parts))

        if any(v.strip() == "" for v in row.values()):
            continue

        try:
            row["LoanPeriod"] = int(row["LoanPeriod"])
            row["Extended"] = int(row["Extended"])
        except ValueError:
            print("Invalid numeric value in row:", row)
            continue

        rows.append(row)

    return rows