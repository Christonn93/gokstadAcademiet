def main():
    try:
        tall = int(input("Type inn a whole number: "))
        for i in range(1, 11):
            print(f"{tall} * {i} = {tall * i}")
    except ValueError:
        print("Please enter a valid whole number.")
