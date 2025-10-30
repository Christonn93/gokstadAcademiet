from collections import defaultdict, Counter
from helpers import read_csv_and_validate

FILENAME = "bokutlån.csv"


def task_5_1(data):
    """Summerer antall dager lånene ble forlenget"""
    total_extensions = sum(row['Forlenget'] for row in data)
    print(f"5.1 TOTAL ANTALL FORLENGETE DAGER: {total_extensions} dager")
    return total_extensions


def task_5_2(data):
    """Beregner hvor mange bøker som er lånt ut per sjanger"""
    genre_count = defaultdict(int)

    for row in data:
        genre_count[row['Sjanger']] += 1

    print("\n5.2 BØKER LÅNT UT PER SJANGER:")
    for genre, count in sorted(genre_count.items()):
        print(f"   {genre}: {count}")

    return dict(genre_count)


def task_5_3(data):
    """Beregner gjennomsnittlig låneperiode inkludert forlengelser"""
    if not data:
        print("\n5.3 GJENNOMSNITTLIG LÅNEPERIODE: Ingen gyldige data")
        return 0

    total_loan_days = sum(row['Låneperiode'] + row['Forlenget'] for row in data)
    average_loan_period = total_loan_days // len(data)

    print(f"\n5.3 GJENNOMSNITTLIG LÅNEPERIODE: {average_loan_period} dager")
    return average_loan_period


def task_5_4(data):
    """Lister opp alle bøkene som ikke ble levert tilbake"""
    not_returned_books = []

    for row in data:
        if row['Tilbakelevert'].lower() == 'nei':
            borrower = f"{row['Fornavn']} {row['Etternavn']}"
            not_returned_books.append((row['Boktittel'], borrower))

    print("\n5.4 BØKER SOM IKKE ER LEVERT TILBAKE:")
    if not_returned_books:
        for book, borrower in not_returned_books:
            print(f"   '{book}' - lånt av: {borrower}")
    else:
        print("   Alle bøker er levert tilbake!")

    return not_returned_books


def task_5_5(data):
    """Finner bøkene som har blitt lånt flest ganger"""
    book_loans = Counter()

    for row in data:
        book_loans[row['Boktittel']] += 1

    print("\n5.5 MEST POPULÆRE BØKER:")
    if book_loans:
        max_loans = max(book_loans.values())
        most_popular_books = [(book, count) for book, count in book_loans.items() if count == max_loans]
        most_popular_books.sort(key=lambda x: x[0])  # Sorter alfabetisk

        for book, count in most_popular_books:
            print(f"   '{book}': {count} lån")

        return most_popular_books
    else:
        print("   Ingen lånedata funnet")
        return []


def main():
    """Hovedfunksjon som kjører alle analysene"""
    print("=" * 50)
    print("BIBLIOTEKSDATA ANALYSE")
    print("=" * 50)

    # Les og valider data
    validated_data = read_csv_and_validate(FILENAME)

    if not validated_data:
        print("Ingen gyldige data å analysere.")
        return

    print(f"Antall gyldige rader: {len(validated_data)}")

    # Kjør alle analysene
    task_5_1(validated_data)
    task_5_2(validated_data)
    task_5_3(validated_data)
    task_5_4(validated_data)
    task_5_5(validated_data)


if __name__ == "__main__":
    main()