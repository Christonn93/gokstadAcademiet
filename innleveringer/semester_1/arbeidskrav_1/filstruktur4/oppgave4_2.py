import os
import shutil
import sys
sys.path.append('filstruktur4')

from oppgave4_1 import create_random_files

def sort_files():
    source_dir = os.path.join("Files")
    target_dir = os.path.join("Files", "SortedFiles")

    if not os.path.exists(source_dir):
        print(f"Error: {source_dir} directory does not exist!")
        print("Creating files first...")
        create_random_files()

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    subdirs = {
        '.txt': 'txt-files',
        '.csv': 'csv-files',
        '.log': 'log-files'
    }

    for subdir in subdirs.values():
        subdir_path = os.path.join(target_dir, subdir)
        if not os.path.exists(subdir_path):
            os.makedirs(subdir_path)

    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

    if not files:
        print("No files found in the Files directory!")
        return

    moved_count = 0

    for filename in files:
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        if ext in subdirs:
            source_path = os.path.join(source_dir, filename)
            target_subdir = os.path.join(target_dir, subdirs[ext])
            target_path = os.path.join(target_subdir, filename)

            shutil.move(source_path, target_path)
            moved_count += 1
            print(f"Moved: {filename} -> {subdirs[ext]}/")

    print(f"\nMoved {moved_count} files to {target_dir}/")

def main():
    print("Task 4.2: Sorting files...")
    sort_files()
    print("File sorting completed!")

if __name__ == "__main__":
    main()