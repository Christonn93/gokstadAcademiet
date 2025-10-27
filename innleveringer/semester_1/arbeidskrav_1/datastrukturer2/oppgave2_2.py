def listSplitting():
    list = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
    list_of_age = []
    list_of_name = []

    try:
        for item in list:
            if isinstance(item, int):
                list_of_age.append(item)
            elif isinstance(item, str):
                    list_of_name.append(item)
    except Exception as e:
        print("An error occurred:", e)
    return list_of_name, list_of_age

def main():
    try:
        list_of_name, list_of_age = listSplitting()
        print("Ages:", list_of_age)
        print("Names:", list_of_name)

    except Exception as e:
        print("An error occurred:", e)


