from datetime import datetime

"""
Prompts the user to enter a date and validates the input format.
Keeps asking until the user provides a valid date in YYYY-MM-DD format.

    :param prompt: The message shown to the user when asking for input.
    :return: A valid date object.
"""
def get_date(prompt):
    # Loop until a valid date is entered
    while True:
        # Get user input as a string
        date_str = input(prompt)
        try:
            # Try converting the string to a date using the format YYYY-MM-DD
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            # If format is wrong or invalid date, show error and repeat
            print("Invalid date format. Please use YYYY-MM-DD.")
