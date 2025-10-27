def main():
    try:
        user_input = int(input("Write a positive whole number: "))
        if user_input <= 0:
            print("You need to write a positive whole number!")
        else:
            total = 0
            for i in range(1, user_input + 1):
                total += i
            print(f"The sum of all whole numbers from 1 to {user_input} is {total}")
    except ValueError:
        print("Invalid input! Please enter a whole number.")
