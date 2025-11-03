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
