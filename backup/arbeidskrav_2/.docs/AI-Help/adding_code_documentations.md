# Adding code documentation

As I'm a front-end developer, I have worked lots on commenting my code to make it easier to understand and increase readability. I'm used to use jsDoc to do this. After searching the web for alternatives to archive similar functionality for pythion
code, I came up empty-handed and decided to ask Deepseek and chatGPT on the best way to hande this. Here is the chat.

---

## Prompt:

I'm used to comment my ts scripts with jsDocs. Currently, I'm learning python for backend development and trying to find out the best way to document my functions.

Here is an example function I have written,

```
"""

"""
class DatabaseConnect:
    @staticmethod
    def connect(host, database, user, password, port, cursor):
        try:
            connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password,
                port=port,
            )
            cursor = connection.cursor()
            print(f"Connection with {host} at {port} is established. You have access to {database} database.")
            print()
            print(f"Provide {user} and {password} to access {database} database.")
            if cursor is not None:
                pass
            else:
                return True
        except Error as err:
            print(err)
```

and that I would like to explain in a similar way as I would have done by using jsDocs.

This is an example of a ts script I have written and used jsDocs on to increase readability and ability.

```ts
/**
 * A custom React hook that determines a page heading based on the current route.
 *
 * It uses the `useLocation` and `useParams` hooks from 'react-router-dom'
 * to get the current pathname and `id` parameter.
 *
 * This hook also has a side effect: it updates the `document.title`
 * to match the calculated heading whenever the heading changes.
 *
 * @returns {string} The calculated heading string for the current page.
 *
 * @example
 * // In a component:
 * const MyComponent = () => {
 * const pageTitle = useHeading();
 * return <h1>{pageTitle}</h1>;
 * }
 */

export const useHeading = () => {
  const { id } = useParams<{ id: string }>();
  const location = useLocation();
  const displayId = id;

  /**
   * Inner helper function to determine the heading string based on the pathname
   * and an optional ID.
   *
   * @param {string} pathname - The current location's pathname.
   * @param {string} [displayId] - The optional 'id' parameter from the route.
   * @returns {string} The corresponding heading string.
   */
  const getHeading = (pathname: string, displayId?: string) => {
    switch (pathname) {
      case "/":
        return "Home";
      case "/about":
        return "About";
      case "/contact":
        return "Contact";
      // Note: Using ?? '' to handle cases where displayId might be undefined
      // even if the path matches /user/
      case `/user/${displayId ?? ""}`:
        return `User ${displayId ?? ""}`;
      default:
        return "Not Found";
    }
  };

  const heading = getHeading(location.pathname, displayId);

  // Effect to update the document title when the heading changes
  useEffect(() => {
    document.title = heading;
  }, [heading]);

  return heading;
};
```

---

## Answer:

Good — this is exactly the kind of mindset that makes your Python code _self-documenting yet accessible._

You’re thinking about **docstrings**, the Pythonic cousin of JSDoc. The idea is the same: you describe **what** a function or class does, **what parameters it takes**, and **what it returns or raises.** But instead of `/** … */`, Python uses triple
quotes (`""" … """`), and docstrings can be introspected at runtime (`help()`, IDEs, Sphinx docs, etc.).

---

Let’s refactor your function to show how it should be documented in Python using **PEP 257** (the docstring convention) and the **Google style** (or **reST/Numpy**—we’ll talk about styles in a second):

### 🧠 Example (Google-style docstring)

```python
import mysql.connector
from mysql.connector import Error

class DatabaseConnect:
    """Handles establishing and managing a connection to a MySQL database."""

    @staticmethod
    def connect(host, database, user, password, port, cursor=None):
        """Establish a connection to a MySQL database.

        This method attempts to connect to a given MySQL database using
        the provided credentials. If successful, it prints connection
        details and returns a cursor object. Errors are printed to stdout.

        Args:
            host (str): The hostname or IP address of the MySQL server.
            database (str): The name of the database to connect to.
            user (str): The username for authentication.
            password (str): The user's password.
            port (int): The port number on which the database is listening.
            cursor (mysql.connector.cursor or None): Optional cursor object to use.

        Returns:
            mysql.connector.connection_text.CMySQLConnection | bool:
                Returns the connection object if successful, otherwise False.

        Raises:
            mysql.connector.Error: If a connection cannot be established.

        Example:
            >>> connection = DatabaseConnect.connect(
            ...     host="localhost",
            ...     database="employees",
            ...     user="admin",
            ...     password="1234",
            ...     port=3306
            ... )
        """
        try:
            connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password,
                port=port,
            )
            cursor = connection.cursor()
            print(f"Connection with {host}:{port} established. Access to {database} granted.")
            return connection
        except Error as err:
            print(f"Database connection failed: {err}")
            return False
```

---

### 🔍 Notes on Python docstring practice

- The **first line** should be a short summary — a single sentence that explains _what_ the thing does.
- Follow it with a blank line, then a more detailed explanation if needed.
- Use `Args:` / `Returns:` / `Raises:` (Google style), or their equivalents in **reStructuredText** (used by Sphinx) or **NumPy style**.
- Tools like **Sphinx**, **pdoc**, or **mkdocstrings** can generate documentation directly from these docstrings.
- IDEs (PyCharm, VS Code, etc.) will automatically display these as hints and hover tooltips.

---

### 📘 Other styles (choose one and stay consistent)

1. **Google Style** Readable, friendly, and what Google and many open-source projects use.

2. **NumPy Style**

   ```
   Parameters
   ----------
   host : str
       Database host.
   ...
   ```

3. **reStructuredText (Sphinx default)**

   ```
   :param host: Database host.
   :type host: str
   :raises Error: If connection fails.
   ```

All three styles express the same info. Pick one, and configure your doc generator (like Sphinx or pdoc) accordingly.

---

If you want, I can show you:

- how to **set up Sphinx or pdoc** to auto-generate HTML docs from these docstrings,
- and how to make your IDE show them like JSDoc comments do in TypeScript.

---

TODO I continued looking into sphinx and pdoc together with chatGPT and decided to test out the pdoc. After installing it, and testing it this is my conclusion !!
