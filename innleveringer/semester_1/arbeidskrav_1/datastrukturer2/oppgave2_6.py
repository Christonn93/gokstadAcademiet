from datastrukturer2.oppgave2_2 import listSplitting

def convert_dataset_to_dict():
    list = listSplitting()

    name_age_dicts = []
    for name, age in zip(list[0], list[1]):
        name_age_dicts.append({name: age})

    return name_age_dicts

def main():
    print(convert_dataset_to_dict())
