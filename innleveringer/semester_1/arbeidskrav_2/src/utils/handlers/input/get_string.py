def get_string(prompt):
    while True:
        try:
            return input(prompt)
        except ValueError:
            print("Please enter a valid string.")