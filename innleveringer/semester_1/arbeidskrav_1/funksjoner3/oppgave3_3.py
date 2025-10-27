def rgb_to_hex(red: int, green: int, blue: int) -> str:
    for value, name in zip((red, green, blue), ("Red", "Green", "Blue")):
        if not isinstance(value, int) or not (0 <= value <= 255):
            raise ValueError(f"{name} value must be an integer between 0 and 255. Got {value}.")
    return f"#{red:02X}{green:02X}{blue:02X}"

def get_rgb_input():
    while True:
        try:
            red = int(input("Enter red (0–255): "))
            green = int(input("Enter green (0–255): "))
            blue = int(input("Enter blue (0–255): "))
            hex_code = rgb_to_hex(red, green, blue)
            print(f"Hex code: {hex_code}")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.\n")

def main():
    get_rgb_input()
