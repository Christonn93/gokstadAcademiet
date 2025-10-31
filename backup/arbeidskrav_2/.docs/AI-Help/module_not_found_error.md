# Understanding the `ModuleNotFoundError`

You are encountering a `ModuleNotFoundError`, which is a common issue in Python. This error occurs when the Python interpreter cannot find a module you are trying to import. Let's break down why this is happening in your project and how to fix it.

## The Error

The traceback you provided shows the following error:

```python
File "C:\Users\Chris\Documents\GitHub\gokstadAcademiet\innleveringer\semester_1\arbeidskrav_2\python\utils\handlers\db_handler.py", line 3, in <module>
    from innleveringer.semester_1.arbeidskrav_2.python.db import setup_database
  File "C:\Users\Chris\Documents\GitHub\gokstadAcademiet\innleveringer\semester_1\arbeidskrav_2\python\db\__init__.py", line 1, in <module>
    from db_config import DB_CONFIG
ModuleNotFoundError: No module named 'db_config'
```

This error originates in `python/db/__init__.py` when it tries to import `DB_CONFIG` from `db_config`. The problem is that Python doesn't know where to find the `db_config` module.

## The Cause

The root cause of this issue is how you are running your Python scripts. It appears you are running a file directly from within the project's directory structure (e.g., `python python/utils/handlers/db_handler.py`). When you do this, Python adds the directory of the script you are running to the system path, but it doesn't know about the overall project structure.

Your project has a specific structure, and the application has a designated entry point, which, according to your `README.md`, is `python/main.py`. This file is responsible for initializing the application and handling imports correctly.

When you run a script from a subdirectory, the relative imports will fail because Python doesn't recognize the root of your project.

## The Solution

To fix this, you should always run your application from its main entry point. In your case, you should run the following command from the root of your project directory:

```bash
python ./python/main.py
```

By doing this, Python will correctly handle the module imports, and you will not encounter the `ModuleNotFoundError`.

### Improving Import Statements

To make your project more robust, it is good practice to use relative imports within your packages. For example, in `python/db/__init__.py`, you can change the import statement from:

```python
from db_config import DB_CONFIG
```

to a relative import:

```python
from .db_config import DB_CONFIG
```

The leading dot tells Python to look for `db_config.py` in the same directory as the `__init__.py` file. This makes your code more modular and less dependent on the project's root directory being in the Python path.

By following these guidelines, you can avoid `ModuleNotFoundError` and create more maintainable Python projects.
