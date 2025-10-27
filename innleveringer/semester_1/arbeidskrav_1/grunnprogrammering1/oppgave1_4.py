def main():
    fruits = ["eple", "banan", "appelsin", "drue", "kiwi"]

    print("Original list:", fruits)
    print("Valid indices are 0 to", len(fruits) - 1)

    try:
        index1 = int(input("Enter first index: "))
        index2 = int(input("Enter second index: "))

        if index1 < 0 or index1 >= len(fruits) or index2 < 0 or index2 >= len(fruits):
            print("Error: One or both indices are invalid")
        else:
            fruits[index1], fruits[index2] = fruits[index2], fruits[index1]
            print("Updated list:", fruits)

    except ValueError:
        print("Error: Please enter valid integers")
