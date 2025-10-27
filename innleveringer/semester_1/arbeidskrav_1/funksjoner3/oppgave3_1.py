def main():
    ip_input = input("Enter ip address: ")

    ip_parts = ip_input.split(".")
    if len(ip_parts) != 4:
        print("Invalid IP address format.")
        return
    try:
        ip_numbers = [int(part) for part in ip_parts]
        if all(0 <= num <= 255 for num in ip_numbers):
            print("Valid IP address")
        else:
            print("invalid IP address")
            return
    except ValueError:
        print("IP address parts must be integers.")
        return
