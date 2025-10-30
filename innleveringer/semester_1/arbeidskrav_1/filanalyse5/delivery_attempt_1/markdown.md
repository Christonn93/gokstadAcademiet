*Good call — splitting this into separate files will keep it structured and easier to manage/test individually.
Here’s how I’d organize it:

* **`read_data.py`** → shared function for reading/validating CSV
* **`oppgave5_1.py`** → sum of forlengelser
* **`oppgave5_2.py`** → count per genre
* **`oppgave5_3.py`** → average loan period
* **`oppgave5_4.py`** → books not returned
* **`oppgave5_5.py`** → most borrowed books
* **`main.py`** → runs all of them in sequence

---

### `read_data.py`

```python
FILENAME = "bokutlan.csv"

def read_data(filename=FILENAME):
    """Read CSV file manually and return list of rows as dicts."""
    rows = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # First line = headers
    headers = lines[0].strip().split(",")

    for line in lines[1:]:
        parts = line.strip().split(",")

        # Skip if not enough columns
        if len(parts) != len(headers):
            continue

        row = dict(zip(headers, parts))

        # Skip rows with missing fields
        if any(v.strip() == "" for v in row.values()):
            continue

        # Try convert numbers
        try:
            row["Låneperiode"] = int(row["Låneperiode"])
            row["Forlenget"] = int(row["Forlenget"])
        except ValueError:
            print("Ugyldig tallverdi i rad:", row)
            continue

        rows.append(row)

    return rows
```

---

### `oppgave5_1.py`

```python
def sum_forlenget(rows):
    total = 0
    for r in rows:
        total += r["Forlenget"]
    print("Totalt antall forlengelsesdager:", total)
    return total
```

---

### `oppgave5_2.py`

```python
def count_by_genre(rows):
    counts = {}
    for r in rows:
        genre = r["Sjanger"]
        if genre not in counts:
            counts[genre] = 0
        counts[genre] += 1

    print("Antall bøker per sjanger:")
    for g in counts:
        print(f"  {g}: {counts[g]}")
    return counts
```

---

### `oppgave5_3.py`

```python
def average_loan_period(rows):
    total_days = 0
    count = 0
    for r in rows:
        total_days += r["Låneperiode"] + r["Forlenget"]
        count += 1
    avg = round(total_days / count) if count > 0 else 0
    print("Gjennomsnittlig låneperiode (inkl. forlengelse):", avg, "dager")
    return avg
```

---

### `oppgave5_4.py`

```python
def not_returned(rows):
    result = []
    for r in rows:
        if r["Tilbakelevert"].lower() == "nei":
            result.append((r["Boktittel"], r["Fornavn"], r["Etternavn"]))

    print("Bøker som ikke ble levert tilbake:")
    for bok, fn, en in result:
        print(f"  {bok} (lånt av {fn} {en})")
    return result
```

---

### `oppgave5_5.py`

```python
def most_borrowed(rows):
    counts = {}
    for r in rows:
        bok = r["Boktittel"]
        if bok not in counts:
            counts[bok] = 0
        counts[bok] += 1

    max_count = max(counts.values()) if counts else 0
    most = [b for b in counts if counts[b] == max_count]

    most.sort()

    print("Mest utlånte bøker:")
    for b in most:
        print(f"  {b}: {counts[b]}")
    return {b: counts[b] for b in most}
```

---

### `main.py`

```python
from read_data import read_data
from oppgave5_1 import sum_forlenget
from oppgave5_2 import count_by_genre
from oppgave5_3 import average_loan_period
from oppgave5_4 import not_returned
from oppgave5_5 import most_borrowed


def main():
    rows = read_data()

    sum_forlenget(rows)
    count_by_genre(rows)
    average_loan_period(rows)
    not_returned(rows)
    most_borrowed(rows)


if __name__ == "__main__":
    main()
```

---

This way you can:

```bash
python main.py
```

…and it will run all tasks. Or you can test each task file independently by importing `read_data` and passing `rows`.

---

Do you want me to also make a **dummy `bokutlan.csv` file** (with 6–7 rows) so you can run these scripts right away and verify the outputs?
*