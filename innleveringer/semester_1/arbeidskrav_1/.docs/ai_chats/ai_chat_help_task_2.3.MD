# Asking Ai for help to understand

Christonn93: Why do I get

Velg oppgave (eks. 1.1), eller 'q' for å avslutte: 2.3

▶ Kjører oppgave 2.3...

❌ Error running datastrukturer2.oppgave2_3.main: No module named 'oppgave2_2'

GitHub Copilot: The error occurs because the import statement in `oppgave2_3.py`:

```python
from oppgave2_2 import list_of_name, list_of_age
```

is trying to import `list_of_name` and `list_of_age` directly from `oppgave2_2.py`. However, these variables are defined inside the `main()` function in `oppgave2_2.py`, so they are not accessible as module-level variables.

Additionally, the import should use the correct module path: since both files are in the datastrukturer2 folder, you should use a relative import or run the script in a way that the folder is in your Python path.

To fix this:

1. Move the creation of `list_of_name` and `list_of_age` to the module level in `oppgave2_2.py` (outside the `main()` function).
2. Or, better: create a function in `oppgave2_2.py` that returns these lists, and import and call that function in `oppgave2_3.py`.
3. Also, use the correct import path: `from datastrukturer2.oppgave2_2 import ...` if running from the project root.

Would you like me to fix the code for you so that `oppgave2_3.py` works as intended?

Christonn93: Just guide me and tell me what i need to do

GitHub Copilot: Absolutely! Here’s what you need to do:

1. **Move the lists out of the `main()` function**
   Define `list_of_name` and `list_of_age` at the top level of oppgave2_2.py (outside any function), so they can be imported.

2. **Fill the lists at the top level**
   Move the code that fills `list_of_name` and `list_of_age` to the top level as well.

**Step-by-step:**

- Open oppgave2_2.py.
- At the top (outside any function), add this code:

  ```python
  # filepath: c:\Users\Chris\OneDrive\Desktop\gokstad_accademiet_school-work\datastrukturer2\oppgave2_2.py
  data = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
  list_of_age = []
  list_of_name = []

  for item in data:
      if isinstance(item, int):
          list_of_age.append(item)
      elif isinstance(item, str):
          list_of_name.append(item)
  ```

- You can keep your `main()` function if you want, but now `list_of_name` and `list_of_age` are available for import.

- In `oppgave2_3.py`, the import will now work.

**Summary:**
You need to define and fill `list_of_name` and `list_of_age` outside of any function in oppgave2_2.py.

Let me know if you want to see the full code!

Christonn93: But I need the oppgave2_2 to be a function also..

GitHub Copilot: Great! You can have both:

- The lists available for import **and**
- A function that prints them.

Here’s how you do it:

1. **Move the list processing to the top level** (outside the function), so the lists are available for import.
2. **Keep your `main()` function** to print the lists.

Here’s how your file should look:

```python
data = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
list_of_age = []
list_of_name = []

for item in data:
    if isinstance(item, int):
        list_of_age.append(item)
    elif isinstance(item, str):
        list_of_name.append(item)

def main():
    try:
        print("Ages:", list_of_age)
        print("Names:", list_of_name)
    except Exception as e:
        print("An error occurred:", e)
```

Now you can:

- Import `list_of_name` and `list_of_age` in `oppgave2_3.py`
- Still run `main()` in oppgave2_2.py to print the lists

Let me know if you need the same for `oppgave2_3.py`!

Christonn93: Velg oppgave (eks. 1.1), eller 'q' for å avslutte: 2.2

▶ Kjører oppgave 2.2...

An error occurred: 'function' object has no attribute 'list_of_age'

GitHub Copilot: You get this error because `list_of_age` and `list_of_name` are **local variables** inside the `listSplitting()` function. They are not accessible as attributes of the function.

**How to fix:**

1. **Return the lists from the function**
   Change `listSplitting()` so it returns both lists.

2. **Unpack the returned values in `main()`**
   Use the returned lists in your `main()` function.

Here’s how you should update your code:

```python
def listSplitting():
    data = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
    list_of_age = []
    list_of_name = []

    try:
        for item in data:
            if isinstance(item, int):
                list_of_age.append(item)
            elif isinstance(item, str):
                list_of_name.append(item)
    except Exception as e:
        print("An error occurred:", e)
    return list_of_name, list_of_age

def main():
    try:
        list_of_name, list_of_age = listSplitting()
        print("Names:", list_of_name)
        print("Ages:", list_of_age)
    except Exception as e:
        print("An error occurred:", e)
```

Now, `main()` will work, and you can also import and use `listSplitting()` from other files.

Christonn93: Velg oppgave (eks. 1.1), eller 'q' for å avslutte: 2.3

▶ Kjører oppgave 2.3...

❌ Error running datastrukturer2.oppgave2_3.main: No module named 'oppgave2_2'

GitHub Copilot: The error `No module named 'oppgave2_2'` means Python cannot find the oppgave2_2.py file as a module.
This usually happens because of **how you run your code** or **your folder structure**.

## How to fix

1. **Use the correct import path**
   If you are running from the project root (`gokstad_accademiet_school-work`), change your import in oppgave2_3.py to:

   ```python
   from datastrukturer2.oppgave2_2 import listSplitting
   ```

2. **Make sure there is an `__init__.py` file**
   In the datastrukturer2 folder, add an empty file named `__init__.py`. This tells Python it’s a package.

3. **Run your script from the project root**
   Open a terminal in `gokstad_accademiet_school-work` and run:

   ```bash
   python -m datastrukturer2.oppgave2_3
   ```

---

**Summary:**

- Change the import to use `datastrukturer2.oppgave2_2`
- Add `__init__.py` in the folder
- Run with `python -m datastrukturer2.oppgave2_3` from the project root
