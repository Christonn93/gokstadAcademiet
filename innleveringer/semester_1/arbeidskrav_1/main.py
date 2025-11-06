import importlib

TASKS = {
    "1.1": ("grunnprogrammering1.oppgave1_1", "main"),
    "1.2": ("grunnprogrammering1.oppgave1_2", "main"),
    "1.3": ("grunnprogrammering1.oppgave1_3", "main"),
    "1.4": ("grunnprogrammering1.oppgave1_4", "main"),
    "1.5": ("grunnprogrammering1.oppgave1_5", "main"),
    "2.1": ("datastrukturer2.oppgave2_1", "main"),
    "2.2": ("datastrukturer2.oppgave2_2", "main"),
    "2.3": ("datastrukturer2.oppgave2_3", "main"),
    "2.4": ("datastrukturer2.oppgave2_4", "main"),
    "2.5": ("datastrukturer2.oppgave2_5", "main"),
    "2.6": ("datastrukturer2.oppgave2_6", "main"),
    "3.1": ("funksjoner3.oppgave3_1", "main"),
    "3.2": ("funksjoner3.oppgave3_2", "main"),
    "3.3": ("funksjoner3.oppgave3_3", "main"),
    "3.4": ("funksjoner3.oppgave3_4", "main"),
    "4": ("filstruktur4.main", "main"),
    "5.1": ("filanalyse5.oppgave5_1", "main"),
    "5.2": ("filanalyse5.oppgave5_2", "main"),
    "5.3": ("filanalyse5.oppgave5_3", "main"),
    "5.4": ("filanalyse5.oppgave5_4", "main"),
    "5.5": ("filanalyse5.oppgave5_5", "main"),
}

def run_task(module_name, func_name="main"):
    """Dynamically import and run a task"""
    try:
        module = importlib.import_module(module_name)
        func = getattr(module, func_name)
        func()
    except Exception as e:
        print(f"❌ Error running {module_name}.{func_name}: {e}")

def run_all_tasks():
    """Run all tasks in order"""
    sorted_tasks = sorted(TASKS.keys(), key=lambda x: (int(x.split(".")[0]), float(x.split(".")[1])))

    for task_key in sorted_tasks:
        module_name, func_name = TASKS[task_key]
        print(f"\n{'='*50}")
        print(f"▶ Running task {task_key}: {module_name}")
        print(f"{'='*50}")
        run_task(module_name, func_name)

def main():
    while True:
        print("\n=== Task Menu ===")
        for key in sorted(TASKS.keys(), key=lambda x: (int(x.split(".")[0]), float(x.split(".")[1]))):
            print(f"{key} -> {TASKS[key][0]}")

        print("\nall -> Run all tasks")

        choice = input("\nSelect task (e.g. 1.1), 'all' to run all, or 'q' to quit: ").strip()

        if choice.lower() == "q":
            print("Exiting. Have a nice day 👋")
            break
        elif choice.lower() == "all":
            print(f"\n▶ Running all tasks...\n")
            run_all_tasks()
            input("\n(↩) Press Enter to return to menu...")
        elif choice in TASKS:
            module_name, func_name = TASKS[choice]
            print(f"\n▶ Running task {choice}...\n")
            run_task(module_name, func_name)
            input("\n(↩) Press Enter to return to menu...")
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
