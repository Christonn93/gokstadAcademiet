# QA Session 1 – Chat with AI (Setup & Project Structure)

**Date:** 2025-09-14
**Topic:** Setting up Python project for Gokstad Akademiet – Backend Programmering (Emne 1)

---

## Conversation Transcript

**User:**
I want each task to be its own file.
can you create a setup.sh file to create folders and files. Make sure that its placed in same order as its in the documents.

**AI:**
Got it. You want a **`setup.sh`** script that builds the full folder + file structure, with one `.py` file per oppgave, in the **same order** as in your document.

(provided script for creating files `1_Grunnprogrammering/oppgave1_1.py …`, etc.)

---

**User:**
I need a main, and make sure each folder have a package file so it all can be runned from the main file.

**AI:**
Perfect — so you want a **Python package-like structure** where:

- Each folder has an `__init__.py`.
- Each oppgave file has a `main()` function.
- A `main.py` at the top level can import and run tasks.

(provided improved `setup.sh` with `__init__.py` and placeholder `main()` functions.)

---

**User:**
Chris@ChrisDev MINGW64 ~/OneDrive/Desktop/gokstad_accademiet_school-work
$ Python main.py
 File "C:\Users\Chris\OneDrive\Desktop\gokstad_accademiet_school-work\main.py", line 1
 from 1_Grunnprogrammering import oppgave1_1
 ^
SyntaxError: invalid decimal literal

**AI:**
Explained Python doesn’t allow package names starting with a digit. Suggested renaming to valid identifiers like `grunnprogrammering1`, `datastrukturer2`, etc.
Provided fixed `setup.sh` with valid package names.

---

**User:**
from grunnprogrammering1 import oppgave1_1
from datastrukturer2 import oppgave2_1
from funksjoner3 import oppgave3_1
from filstruktur4 import oppgave4_1
from filanalyse5 import oppgave5_1

def main():
 print("Velkommen til Oppgave-systemet!")
 print("Kjører en oppgave fra hvert kapittel som eksempel:")

    // I want to run a function that allow the usert to pick a tasak from the list of tasks. Then run it and return to the list on enter click after task have runned.

if **name** == "**main**":
 main()

**AI:**
Explained how to build a **menu-driven CLI** using `importlib`.
Provided `main.py` code that dynamically lists tasks, lets the user pick (`1.1`, `2.3`, etc.), runs the task’s `main()`, and returns to the menu after pressing Enter.

---

**User:**
Please, create a readme outlining the setup, and includes a space for adding links to files containing detailed copy of QA i have had with ai. This needs to be included on delivery to avoid plaigeraitions.

**AI:**
Created `README.md` with:

- Project structure.
- Setup instructions.
- How to run tasks.
- Section for linking QA transcripts.

---

**User:**
Give me a full markdown file of this chat.

**AI:**
(Delivered this file.)

---

## Notes

- All scripts (`setup.sh`, `main.py`, oppgave files) are **AI-assisted scaffolding**, but the actual task solutions must be written by the student.
- QA transcripts like this are included in `docs/` to prove originality and avoid plagiarism.
- Folder names were adjusted (`grunnprogrammering1` instead of `1_Grunnprogrammering`) because Python identifiers cannot start with digits.

---

## End of Session
