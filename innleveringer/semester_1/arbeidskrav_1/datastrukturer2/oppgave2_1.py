def is_valid_date(date_input):
    try:
        day, month, year = map(int, date_input.split('/'))
    except ValueError:
        return False

    if year < 1 or year > 9999:
        return False

    if month < 1 or month > 12:
        return False

    days_in_month = [31, 28 + (1 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 0),
                     31, 30, 31, 30,
                     31, 31, 30,
                     31, 30, 31]

    if day < 1 or day > days_in_month[month - 1]:
        return False

    return True


def main():
    while True:
        date_input = input("Enter a date (dd/mm/yyyy): ")
        if is_valid_date(date_input):
            print("Date is valid")
            break
        else:
            print("Date not valid. Please try again.")

if __name__ == "__main__":
    main()
