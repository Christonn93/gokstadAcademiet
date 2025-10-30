import os
import random
import string

def create_random_files():
    """
    Oppretter en mappe kalt 'Files' og genererer 30 tilfeldige filer.
    Filtypene er .txt, .csv og .log.
    Sørger for at 30 unike filer faktisk blir laget, selv om navn kan overlappe.
    """
    files_dir = os.path.join("filstruktur4", "Files")
    os.makedirs(files_dir, exist_ok=True)

    extensions = ['.txt', '.csv', '.log']
    created_files = 0
    attempts = 0

    # Bruk while-løkke slik at vi får nøyaktig 30 filer uansett duplikater
    while created_files < 30:
        attempts += 1
        name_length = random.randint(5, 10)
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_length))
        random_extension = random.choice(extensions)
        filename = random_name + random_extension
        filepath = os.path.join(files_dir, filename)

        if not os.path.exists(filepath):
            with open(filepath, 'w') as file:
                file.write(f"This is a {random_extension} file named {random_name}\n")
                file.write(f"Generated file #{created_files + 1}\n")
            created_files += 1

    print(f"Laget {created_files} unike filer i {files_dir}/ etter {attempts} forsøk.")

def main():
    print("Task 4.1: Oppretter tilfeldige filer...")
    create_random_files()
    print("Filoppretting ferdig!")

if __name__ == "__main__":
    main()
