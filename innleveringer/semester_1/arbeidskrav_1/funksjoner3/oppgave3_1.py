def split_input(arg: str):
    """Split IP address string by dots into individual parts"""
    return arg.split(".")


def main(ip_input: str) -> None:
    # Run a check on the input
    if not ip_input:
        print("Please enter your ip address")
    elif len(ip_input) == 4:
        print("Invalid ip address")

    try:
        # Splitting ip address into its four octets
        ip_parts = split_input(ip_input)

        # Convert each octet from string to integer
        ip_numbers = [int(part) for part in ip_parts]

        # Check if all octets are within valid IP address range (0-255)
        if all(0 <= num <= 255 for num in ip_numbers):
            print("Entered a valid ip address")
        else:
            print("Invalid ip address")

    except ValueError:
        print("Invalid ip address")

if __name__ == "__main__":
    main(input("Enter ip address: "))