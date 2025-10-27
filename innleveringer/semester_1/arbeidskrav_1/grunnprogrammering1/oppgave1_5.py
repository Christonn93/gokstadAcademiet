def main():
    try:
        number = int(input("Type in a whole number: "))
        m = int(input("Start of interval (m): "))
        n = int(input("End of interval (n): "))

        if m > n:
            print("Start of interval must be less than or equal to end of interval.")
            return

        print("\nMultiplication Table:")
        header = [str(i).rjust(4) for i in range(m, n + 1)]
        print("    " + "".join(header))
        print("    " + "-" * (4 * (n - m + 1)))

        for i in range(m, n + 1):
            row = [str(i * j).rjust(4) for j in range(m, n + 1)]
            print(str(i).rjust(3) + "|" + "".join(row))

    except ValueError:
        print("Please enter valid whole numbers.")
