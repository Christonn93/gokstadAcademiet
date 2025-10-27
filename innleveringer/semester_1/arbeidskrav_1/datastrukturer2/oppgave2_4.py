from datastrukturer2.oppgave2_3 import create_dict

def sort_dict_by_age(name_age_dict):
    return dict(sorted(name_age_dict.items(), key=lambda item: item[1], reverse=True))


def main():
    name_age_dict = create_dict()
    sorted_dict = sort_dict_by_age(name_age_dict)
    for name, age in sorted_dict.items():
        print(f"{name} is {age} years old")