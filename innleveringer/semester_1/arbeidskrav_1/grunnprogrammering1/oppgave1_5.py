def main():
    try:
        m = int(input("Start of interval (m): "))
        n = int(input("End of interval (n): "))

        if m > n:
            print("Start of interval must be less than or equal to end of interval.")
            return

        # Dynamic width calculation
        max_value = n * n
        width = len(str(max_value)) + 2

        print("\nMultiplication Table:")
        header_cells = [f"{j:>{width}}" for j in range(m, n + 1)]
        print(" " * width + "".join(header_cells))
        print(" " * width + "-" * (width * (n - m + 1)))

        # Build table rows
        for i in range(m, n + 1):
            row_cells = [f"{i * j:>{width}}" for j in range(m, n + 1)]
            print(f"{i:>{width-1}}|" + "".join(row_cells))

    except ValueError:
        print("Please enter valid whole numbers.")

if __name__ == "__main__":
    main()