import os

def is_valid_seed_file(file_path: str):
    """Validate input parameters for seeding operation """
    if not file_path:
        print("ERROR: No SQL file provided for seeding.")
        return False

    if not os.path.exists(file_path):
        print(f"ERROR: SQL file not found: {file_path}")
        return False

    return True