import os
import random
import string

def create_random_files():
    files_dir = os.path.join("filstruktur4", "Files")
    if not os.path.exists(files_dir):
        os.makedirs(files_dir)
    else:
        print("Files directory already exists. Adding new files...")
    extensions = ['.txt', '.csv', '.log']
    for i in range(30):
        name_length = random.randint(5, 10)

        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_length))

        random_extension = random.choice(extensions)

        filename = random_name + random_extension
        filepath = os.path.join(files_dir, filename)

        if not os.path.exists(filepath):
            with open(filepath, 'w') as file:
                file.write(f"This is a {random_extension} file named {random_name}\n")
                file.write(f"Generated file #{i+1}\n")

    print(f"Created/verified 30 random files in {files_dir}/")

def main():
    print("Task 4.1: Creating random files...")
    create_random_files()
    print("File creation completed!")

if __name__ == "__main__":
    main()