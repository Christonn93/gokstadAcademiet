import os

# Read csv file
# Store contents in list
def read_text_file(filename: str) -> list[str]:
    """
    Reads text content of a file and returns it as a list.
    :param filename: The name of the file to read from.
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            return [line.strip('\n') for line in f]
    except FileNotFoundError as e:
        print(f"Error in function read_text_file: {e}")
        return []


def parse_csv(filename: str) -> list[dict]:
    file_contents = read_text_file(filename)
    print(file_contents)
    output = []
    errors: list[str] = []

    # Skip header
    # print(list(enumerate(file_contents)))
    for index, line in enumerate(file_contents):
        if index == 0:
            continue

        # Trim leading/trailing whitespace, then split the line on commas
        try:
            # pet_name, race, is_mammal = line.strip().split(',')
            pet_name, race, is_mammal = [item.strip() for item in line.split(',')]

            # Validation methods are called here
            bool_is_mammal = parse_bool(is_mammal)

            output.append(
                {
                    'pet_name': pet_name,
                    'race': race,
                    'is_mammal': bool_is_mammal
                })
        except ValueError as e:
            error_message = f"Error in line {index + 1}: {e}. Line content: {line}"
            errors.append(error_message)

    if errors:
        print(f"\nProcessed with {len(errors)} error(s):")
        for error in errors:
            print(error)

    return output


# Validate bool column
def parse_bool(input_str: str, ) -> bool:
    """
    Converts an input string to a boolean based on whether it matches a given 'ja' or 'nei' string.
    :param input_str: The input string to parse.
    :return: True if the input string matches 'ja', False if 'nei'.
    """
    if input_str.lower() == 'yes':
        return True
    elif input_str.lower() == 'no':
        return False
    raise ValueError(f"Invalid boolean string: '{input_str}'. Expected 'yes' or 'no'.")


if __name__ == '__main__':
    data = parse_csv('pets.csv')
    print(f"\n{data}")

    # print(data)



def handle_input_num(prompt: str) -> int | float | None:
    while True:
        user_input = input(prompt)

        if user_input.strip() == '':
            print('Input is required, please try again.')
            continue
        try:
            return float(user_input)
        except ValueError:
            print(f'"{user_input}" cannot be converted to a number. Please enter a valid number.')


def handle_num_casting(number: int | float) ->  int | float:
    if number % 1 > 0:
        return float(number)
    else:
        return int(number)


def check_if_negative_or_positive() -> str:
    casted_number = handle_num_casting(handle_input_num('Enter a number: '))

    if casted_number < 0:
        return f'{casted_number} is a negative number.'
    elif casted_number > 0:
        return f'{casted_number} is a positive number.'
    else:
        return f'{casted_number} is zero.'


print(check_if_negative_or_positive())





import mysql.connector
from mysql.connector import Error

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "gokstad",
    "database": "musikk",
    "port": 3306
}

def get_connection():
    try:
        conn = mysql.connector.connect(**db_config)

        if conn.is_connected():
            print(f"\nConnected to MySQL database\n")
            return conn
    except Error as e:
        print(f"\nConnection error: {e}")
        return None


def select(table: str) -> list[tuple] | None:
    conn = get_connection()
    if not conn:
        return None

    cursor: object = None

    try:
        cursor: object = conn.cursor()
        cursor.execute(f"SELECT * FROM {table};")

        rows: list[tuple] = cursor.fetchall()
        print(f"Table {table}:")
        for row in rows:
            print(row)

        return rows

    except Error as e:
        print(f"Query error: {e}")
    finally:
        if cursor:
            cursor.close()
        conn.close()
        print("\nConnection closed")


if __name__ == "__main__":
    select("eleev")