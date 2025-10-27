# Gokstad Academy – Backend Programming (Subject 1)

This repository contains the assignment solutions for **Backend Programming, Subject 1**.
All assignments are structured in separate folders and files, and the project is set up as a Python package project with a menu-based `main.py` that lets you select and run assignments dynamically.

---

## 📂 Project Structure

```bash
.
├── main.py                 # Menu system for running assignments
├── bokutlan.csv            # Empty CSV file used in File Analysis assignments
├── grunnprogrammering1/    # Chapter 1 – Basic Programming
│   ├── **init**.py
│   ├── oppgave1\_1.py
│   └── ...
├── datastrukturer2/        # Chapter 2 – Data Structures
│   ├── **init**.py
│   ├── oppgave2\_1.py
│   └── ...
├── funksjoner3/            # Chapter 3 – Functions
│   └── ...
├── filstruktur4/           # Chapter 4 – File Structure
│   └── ...
└── filanalyse5/            # Chapter 5 – File Analysis
└── ...
```

---

## ⚙️ Setup

1. Make sure you have **Python 3.10+** installed.
2. Run `setup.sh` (only the first time) to create folder structure and files:

   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. Start the menu:

   ```bash
   python main.py
   ```

---

## ▶️ Usage

* The program displays a list of all assignments (e.g. `1.1`, `2.3`, etc.).
* Enter the number of the assignment you want to run.
* The assignment's `main()` function runs.
* Press **Enter** to return to the menu.
* Type `q` to exit.

---

## 📑 QA Documentation

To ensure that the work is original and avoid plagiarism, an archive of conversations and guidance from AI has been created.
Links to these documents (either in PDF, Markdown, or other format) should be placed here:

* [Project init chat](ai_chats/ProjectInit.MD)
* [Help with task 2_1](ai_chats/ai_help_oppgave2_1.MD)

---

## External links used for task solving

### Task 2_1

[Datevalidation_1](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
[Datevalidation_2](https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python)

---

## 👨‍💻 Author

Student: *[Christopher Tønnesland]*
Subject: Backend Programming (Subject 1)
School: Gokstad Academy
Delivery Period: **August 29, 2025 – October 3, 2025**
