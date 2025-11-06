def get_string(prompt: str) -> str:
    """
    Prompt the user for a string input.
    Continues prompting until a valid non-empty string is provided.

    :param prompt: The message shown to the user when asking for input.
    :return: String value entered by the user.
    """
    while True:
        try:
            value = input(prompt)
            if value.strip():
                return value
            print("⚠️ Input cannot be empty. Please enter text.")
        except Exception as ex:
            print(f"❌ Unexpected error. Please enter a valid string. {ex}")


def get_int(prompt: str) -> int:
    """
    Prompt the user for an integer input.
    Keeps asking until the user enters a valid number.

    :param prompt: The message shown to the user when asking for input.
    :return: Integer value entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("⚠️ Invalid input. Please enter a whole number.")


from datetime import datetime

def get_date(prompt: str):
    """
    Prompt the user to enter a valid date in YYYY-MM-DD format.
    Keeps asking until the user provides a valid date.

    :param prompt: The message shown to the user when asking for input.
    :return: A valid datetime.date object.
    """
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("⚠️ Invalid date format. Please use YYYY-MM-DD (e.g., 2024-05-17).")
