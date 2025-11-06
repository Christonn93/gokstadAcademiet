import os
import random
import string
import shutil
import time

from utils.terminal import styled_print, clear_and_header, elevator_music

# Define the main folders for file generation and sorting
source_dir = os.path.join("Files")
target_dir = os.path.join(source_dir, "SortedFiles")

# === Utils functions ===
def is_existing(filepath: str) -> bool:
    """Check whether a file already exists."""
    return os.path.exists(filepath)     # Return True if file exists, False otherwise

def count_files(directory: str) -> int:
    """Count number of files in a directory (non-recursive)."""
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return len(files)     # Return how many files (not folders) exist in the directory

def generate_folder(folder_name: str) -> None:
    """Ensure that the main 'Files' folder exists."""
    os.makedirs(folder_name, exist_ok=True)     # Create the folder if it doesn’t already exist

def get_file_extension(file_name: str) -> str | None:
    """Get file extension from file name."""
    try:
        _, file_extension = os.path.splitext(file_name)
        file_extension = file_extension.lower()  # Convert to lowercase for consistency
        return file_extension
    except Exception as e:
        print(f"{e}")
        return None

def generate_names() -> str:
    """Generate a random alphanumeric filename (without extension)."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 10)))

def generate_extensions() -> str:
    """Randomly select a file extension."""
    extensions = ['.log', '.csv', '.txt',]     # Predefined list of extensions
    return random.choice(extensions)

def generate_file_names() -> str:
    """Combine a random filename and extension into a tuple."""
    return generate_names() + generate_extensions()

def get_subfolder_mapping():
    """Generate a dictionary that maps file extensions to folder names dynamically."""
    # Scan source_dir to find all unique extensions
    extensions_found = set()
    if is_existing(source_dir):
        for entry in os.scandir(source_dir):
            if entry.is_file():
                ext = get_file_extension(entry.name)
                if ext:
                    extensions_found.add(ext)

    # Create dynamic mapping: .txt -> txt, .csv -> csv, etc.
    mapping = {}
    for ext in extensions_found:
        # Remove the dot and use as folder name
        folder_name = ext[1:]  # .txt becomes txt
        mapping[ext] = folder_name

    return mapping

def file_sorter(entry, mapping, counter_list, amount):
    """Move a single file from source folder into correct subfolder by extension."""
    try:
        if entry.is_file():
            file_extension = get_file_extension(entry.name)
            if file_extension in mapping:
                subfolder = mapping[file_extension]
                destination_folder = os.path.join(target_dir, subfolder)
                destination_path = os.path.join(destination_folder, entry.name)

                os.rename(entry.path, destination_path)
                counter_list[0] += 1
                step_counter("Moving files", counter_list, amount)
    except PermissionError as e:
        print(f"Permission denied: {e}")

def generate_sorted_folders():
    """Create the 'SortedFiles' folder with subfolders based on found file types."""
    os.makedirs(target_dir, exist_ok=True)  # Create SortedFiles folder
    mapping = get_subfolder_mapping()
    for folder_name in mapping.values():
        folder_path = os.path.join(target_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

def step_counter(print_message: str, count_list: list, base_count: int) -> None:
    """Display progress counter on same line."""
    print(f"\r{print_message}: {count_list[0]} / {base_count}", end="", flush=True)

def clean_up_service():
    """Clean up service to give the Veileder a clean slate if I forgot to delete the files folder before zipping it up."""
    if is_existing(source_dir):
        styled_print("🧼 Let's clean up first.. 🧹🧽", "info")

        # Ask for confirmation first
        response = input(f"Directory '{source_dir}' exists. Do you want to delete it? (y/n): ")
        if response.lower() not in ['y', 'yes']:
            styled_print("Directory deletion cancelled.", "warning")
            print("🤔😅🙃 No worries, we can try again! 🙃😅🤔")
            return False

        # Now show the cleanup animation AFTER user says yes
        print()  # New line
        cleanup_actions = ["🧯 Extinguishing fires...", "🧹 Sweeping dust...", "✨ Polishing surfaces...",
                           "🧽 Wiping clean...", "🗑️ Taking out trash..."]
        for action in cleanup_actions:
            print(f"\r{action}", end="", flush=True)
            time.sleep(0.5)
        print()  # New line

        # Proceed with actual deletion
        try:
            shutil.rmtree(source_dir)
            if not is_existing(source_dir):
                styled_print(f"✅ Successfully deleted directory: {source_dir}", "success")
                return True
            else:
                styled_print(f"⚠️ Warning: Directory may not be fully deleted: {source_dir}", "warning")
                return False
        except PermissionError as e:
            styled_print(f"❌ Permission denied: {e}", "error")
            return False
        except Exception as e:
            styled_print(f"❌ Error deleting directory: {e}", "error")
            return False
    else:
        print("✅ No existing directory to clean up.")
        print("🎯🎯🎯 We're already sparkling clean! 🎯🎯🎯")
        print("✨🌟⭐ Like a brand new canvas! ⭐🌟✨")
        return True

# === Task 4.1: File generation ===
def create_files():
    """Generate 30 unique random files inside 'Files' folder."""

    # Default variables
    created_files: int = 0
    expected_file_amount: int = 30

    # Ensure the base folder exists FIRST
    if not is_existing(source_dir):
        print(f"Folder do not exist. Creating...\n")
        generate_folder(source_dir)

    # NOW count files after folder exists
    file_count = count_files(source_dir)

    try:
        # Check if directory contains 30 files
        while file_count >= expected_file_amount:
            print(f"{source_dir} already exists. And contains {file_count} files.\n")
            return

        # Keep creating files until 30 unique names are reached
        while created_files < 30:
            file_name = generate_file_names()
            file_path = os.path.join(source_dir, file_name)

            # Skip file if name already exists
            if not is_existing(file_path):
                # Write basic content to the file
                with open(file_path, "w") as file:
                    file.write("")  # Empty content as required
                created_files += 1
                step_counter("Creating files", [created_files], expected_file_amount)
                time.sleep(0.1)  # Small delay between file creations

        print(f"\n✅ Successfully created {created_files} files\n")
        time.sleep(1)  # Pause after completion
    except PermissionError as e:
        print(f"Permission denied: {e}")

# === Task 4.2: File sorting ===
def sort_all_files():
    """Orchestrate the file sorting process."""
    global target_dir
    target_dir = os.path.join(source_dir, "SortedFiles")

    generate_sorted_folders()
    mapping = get_subfolder_mapping()

    amount = len([f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))])
    counter_list = [0]  # Use list to make counter mutable

    # Sort each file
    for entry in os.scandir(source_dir):
        if entry.is_file():
            file_sorter(entry, mapping, counter_list, amount)
            time.sleep(0.2)

# === Main program function ===
def main():
    """Program entry point."""
    styled_print("Welcome to the File Sorting Program!", "header")
    time.sleep(2)
    clear_and_header("🧹 CLEANUP PHASE")

    clean_up_service()
    time.sleep(2)

    clear_and_header("📁 TASK 4.1: FILE GENERATION")
    elevator_music()

    create_files()
    time.sleep(2)

    clear_and_header("📂 TASK 4.2: FILE SORTING")
    elevator_music()

    sort_all_files()

    print("\n")
    styled_print("🎉 Program completed successfully!", "success")
    time.sleep(2)

# Run program
if __name__ == "__main__":
    main()
