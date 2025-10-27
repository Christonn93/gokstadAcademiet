from datastrukturer2.oppgave2_2 import listSplitting

def create_dict():
    list_of_name, list_of_age = listSplitting()
    name_age_dict = dict(zip(list_of_name, list_of_age))
    return name_age_dict

def main():
    name_age_dict = create_dict()
    for name, age in name_age_dict.items():
        print(f"{name} is {age} years old")
