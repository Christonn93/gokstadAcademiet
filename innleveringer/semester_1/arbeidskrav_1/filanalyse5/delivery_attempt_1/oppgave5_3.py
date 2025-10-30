def average_loan_period(rows):
    total_days = 0
    count = 0
    for r in rows:
        total_days += r["LoanPeriod"] + r["Extended"]
        count += 1
    avg = round(total_days / count) if count > 0 else 0
    print("Average loan period (incl. extension):", avg, "days")
    return avg

def main():
    rows = [
        {"LoanPeriod": 14, "Extended": 3},
        {"LoanPeriod": 7, "Extended": 0},
        {"LoanPeriod": 21, "Extended": 7}
    ]
    average_loan_period(rows)