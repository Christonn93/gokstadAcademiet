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
