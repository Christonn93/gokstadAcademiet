def main():
    try:
        input_str_1 = input("Type inn a sentence: ")
        input_str_2 = input("Type inn another sentence: ")
        if not input_str_1 or not input_str_2:
            print("You need to type in two sentences!")
        else:
            if input_str_1 == input_str_2:
                print("The sentences are identical.")
                print(f"Both sentences have {len(input_str_1)} characters.")
            else:
                print("The sentences are different.")
                print(f"The first sentence has {len(input_str_1)} characters.")
                print(f"The second sentence has {len(input_str_2)} characters.")
    except Exception as e:
        print(f"An error occurred: {e}")
