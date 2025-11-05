"""
Prompt the user for a string input.
Continues prompting until a valid non-empty string is provided.

    :param prompt: The message shown to the user when asking for input.
    :return: String value entered by the user.
"""

def get_string(prompt):
        # Repeat until valid input
    while True:
        try:
            # Read input as string
            value = input(prompt)
                # Ensure it's not just empty spaces
            if value.strip():
                return value
            else:
                print("Input cannot be empty. Please enter text.")
        except ValueError:
            # In rare cases input() could fail
            print("Please enter a valid string.")


"""
Prompt the user for an integer input.
Keeps asking until the user enters a valid number.

    :param prompt: The message shown to the user when asking for input.
    :return: Integer value entered by the user.
"""

def get_int(prompt):
        # Repeat until valid input
    while True:
        try:
            # Try converting input to integer
            return int(input(prompt))
        except ValueError:
            # Error message if conversion fails
            print("Invalid input. Please enter a number.")


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
