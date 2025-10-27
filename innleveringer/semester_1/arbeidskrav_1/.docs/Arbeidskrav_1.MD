
# Backend Programming – Module 1

## Basic Programming

### Cybersecurity – Module 1

#### Introduction to Programming – Python

### Assignment 1

- **Time:** August 29, 2025 – October 3, 2025
- **Aids:** All
- **Attachment:** File: `bokutlån.csv`
- **Submission:** Python files are submitted together in a `.zip` file

---

## 1. Basic Programming

### Task 1.1

Create a program that asks the user to enter a positive integer (`int`) and finds the sum of all numbers from 1 to this number (inclusive). The sum should be calculated using a **for loop**.

### Task 1.2

Write a program that asks the user to enter **two sentences**. The program should then compare the length of the two sentences and print which one is longer and the number of characters in that sentence.

### Task 1.3

Create a program that asks the user to enter a number and generates the **multiplication table** for that number (from 1 to 10).

Example:

```python
Input: 3
Output: 
3 * 1
3 * 2
3 * 3
...
```

### Task 1.4

Create a program that swaps two elements in a given list. The program should use the following list:

```python
    fruits = ["eple", "banan", "appelsin", "drue", "kiwi"]
```

1. Ask the user to enter two indices (input).
2. Swap the elements at the specified indices.
3. Print the updated list.

If one or both indices are invalid, the program should give an appropriate error message.

### Task 1.5

Extend **Task 1.3** so that the user can specify an interval `[m, n]` instead of 1–10. The program should print a nicely formatted table for the number in the entire interval.

Example:

|     | 1   | 2   | 3   |
| --- | --- | --- | --- |
| 1   | 2   | 3   |     |
| 2   | 4   | 6   |     |
| 3   | 6   | 9   |     |

---

## 2. Data Structures

### Task 2.1

Write a program that reads a date in the format `dd/mm/yyyy` from the user. The program should check if the date is valid. If the date is invalid, an error message should be given.

### Task 2.2

Given the list:

```python
["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
```

Write a program that splits this list into two separate lists: one with names and one with ages.

### Task 2.3

Use the lists from **Task 2.2** and create a **dictionary** where names are keys and ages are values.

Example output:

```bash
    Cecilie is 28 years old
    Bjørn is 30 years old
```

### Task 2.4

Write a program that sorts this dictionary by **age** so that the oldest comes first.

### Task 2.5

Starting from the dictionary from **Task 2.4**, create a new list with the same format as in **Task 2.2**, but sorted by **name**.

Example:

```python
    ["Anna", 25, "Bjørn", 30, "Cecilie", 28, "Tor", 24]
```

### Task 2.6

Convert the dataset from **Task 2.2** to a list of dictionaries:

```python
    {"name": "Cecilie", "age": 28}
```

---

## 3. Functions

### Task 3.1

Create a function that takes a string and checks if it is a **valid IPv4 address**.

- Valid address = four parts, separated by dots, each part between 0 and 255.
- Return `True` if valid, otherwise `False`.

Example:

```bash
    Input: "192.168.0.1" → Output: True
    Input: "256.100.50.0" → Output: False
```

### Task 3.2

Create a function that takes **two dates** in the format `dd/mm/yyyy` and returns the number of days between them.

- If the first date is later than the second, the function should still return a positive number.

Example:

```bash
    Input: "21/11/2024", "01/01/2024" → Output: 325 days
```

### Task 3.3

Create a function `rgb_to_hex` that takes three integers (`red`, `green`, `blue`) and returns the corresponding **hex code** as a string.

- Example: `(205, 92, 92)` → `#CD5C5C`.
- Add an error message if the parameters have invalid values (not between 0–255).

### Task 3.4

Create a function that takes another function as a parameter, some arguments, and an expected result. It should return **true** if the result matches, otherwise **false**.

---

## 4. Create File Structure and Sort Files

### Task 4.1

Create a function that creates a folder called `Files` and generates **30 random files** with file types `.txt`, `.csv`, and `.log`.

- Random name: 5–10 characters
- Random file type from the three mentioned
- The content is not important

Example:

```bash
Files
|-- G5zLehz4.txt
|-- iTwTrTkU.txt
|-- vPcaO7jR.csv
|-- 1Vgi2jbe.log
`-- 7NMaq7aa.csv
```

### Task 4.2

Create a function that reads the files in `Files` and sorts them into subfolders based on file type.

- Create folder `SortedFiles`
- Create subfolders `txt-files`, `csv-files`, `log-files`
- Move the files there

Example:

```bash
SortedFiles
|-- csv
|   |-- vPcaO7jR.csv
|   `-- 7NMaq7aa.csv
|-- log
|   `-- 1Vgi2jbe.log
`-- txt
    |-- G5zLehz4.txt
    `-- iTwTrTkU.txt
```

---

## 5. File Analysis

You have access to the file `bokutlån.csv`. It contains information about books that have been borrowed from a library.

### Columns

1. First name
2. Last name
3. Book title
4. Genre (Fiction, Crime, Non-fiction, Fantasy)
5. Loan date (`dd/mm/yyyy`)
6. Loan period (standard: 14 days)
7. Extended (extra days, can be 0)
8. Returned (Yes/No)

### The program should handle

- **Missing data:** ignore the row, but continue calculations
- **Invalid values:** handle with error message

Tip:

```python
    open(filename, 'r', encoding='utf-8')
```

---

### Task 5.1

Write a program that sums the number of days the loans were **extended** and prints the answer.

### Task 5.2

Create a function that calculates how many books are borrowed per genre.

Example:

```bash
    Fantasy: 3
    Crime: 5
```

### Task 5.3

Calculate the **average loan period** (including extensions).

### Task 5.4

Create a function that lists all books that **were not returned**. Return a list with book titles and names of the borrowers.

### Task 5.5

Create a function that finds which books have been **borrowed the most times**.

- Return an overview with book titles and the number of times they have been borrowed.
- If several books are equally popular, sort alphabetically.

---
