from datetime import datetime

def days_between(date1: str, date2: str) -> int:
    try:
        d1 = datetime.strptime(date1, "%d/%m/%Y")
        d2 = datetime.strptime(date2, "%d/%m/%Y")
        delta = abs((d1 - d2).days)
        return delta
    except ValueError:
        raise ValueError("Invalid date format or value. Use dd/mm/yyyy.")

def main():
    while True:
        date1 = input("Enter the first date (dd/mm/yyyy): ")
        date2 = input("Enter the second date (dd/mm/yyyy): ")

        try:
            days = days_between(date1, date2)
            print(f"There are {days} days between {date1} and {date2}.")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.\n")

if __name__ == "__main__":
    main()
