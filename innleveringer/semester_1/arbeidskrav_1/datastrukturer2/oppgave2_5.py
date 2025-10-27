from datastrukturer2.oppgave2_3 import create_dict

def sortListByName():
    name_age_dict = create_dict()
    sorted_by_name_list = []

    for name in sorted(name_age_dict.keys()):
        sorted_by_name_list.append(name)
        sorted_by_name_list.append(name_age_dict[name])

    print(sorted_by_name_list)


def main():
    sortListByName()
