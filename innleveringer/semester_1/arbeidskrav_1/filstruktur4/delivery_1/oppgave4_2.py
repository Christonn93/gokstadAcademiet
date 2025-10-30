import os
import shutil
from oppgave4_1 import create_random_files

def sort_files():
    """
    Leser filene i 'filstruktur4/Files' og sorterer dem i undermapper
    etter filtype i 'filstruktur4/SortedFiles'.
    Mappene lages dynamisk basert på faktiske filtyper i mappen.
    """
    base_dir = "filstruktur4"
    source_dir = os.path.join(base_dir, "Files")
    target_dir = os.path.join(base_dir, "SortedFiles")

    # Sjekk at kildemappen finnes, ellers opprett filer
    if not os.path.exists(source_dir):
        print(f"Mappen {source_dir} finnes ikke. Lager filer først...")
        create_random_files()

    os.makedirs(target_dir, exist_ok=True)

    # Finn alle filer i Files-mappen
    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    if not files:
        print("Ingen filer funnet i 'Files'-mappen.")
        return

    moved_count = 0

    for filename in files:
        _, ext = os.path.splitext(filename)
        ext = ext.lower().strip('.')

        # Lag undermappe dynamisk basert på filtype
        subdir_path = os.path.join(target_dir, f"{ext}-files")
        os.makedirs(subdir_path, exist_ok=True)

        source_path = os.path.join(source_dir, filename)
        target_path = os.path.join(subdir_path, filename)

        shutil.move(source_path, target_path)
        moved_count += 1
        print(f"Flyttet: {filename} → {ext}-files/")

    print(f"\nTotalt flyttet {moved_count} filer til {target_dir}/")

def main():
    print("Task 4.2: Sorterer filer...")
    sort_files()
    print("Fil-sortering ferdig!")

if __name__ == "__main__":
    main()
