import mysql.connector
from mysql.connector import Error
from PrintResult import *

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "gokstad",
    "database": "musikk",
    "port": 3306
}

def get_connection():
    try:
        conn = mysql.connector.connect(**db_config)

        if conn.is_connected():
            # print(f"\nConnected to MySQL database\n")
            return conn
    except Error as e:
        # print(f"\nConnection error: {e}")
        return None


def send_query(query_string, params: tuple | None = None) -> list[dict]:
    conn = get_connection()
    if not conn:
        print("No connection")
        return None

    cursor: object = None

    try:
        cursor: object = conn.cursor(dictionary=True)
        cursor.execute(query_string, params)

        if cursor.description:
            rows: list[dict] = cursor.fetchall()
            return rows
        else:
            conn.commit()
            return cursor.rowcount

    except Error as e:
        print(f"Query error: {e}")
    finally:
        if cursor:
            cursor.close()
        conn.close()
        # print("Connection closed")

    return None


def instrument_lanerhistorikk(renter_id: int) -> list[list[dict]]:
    renter = send_query(
        f"SELECT e.Fornavn, e.Etternavn, e.Adresse, i.Navn, i.Type, u.Utlaansdato, u.Levert "
        f"FROM elev e "
        f"JOIN utlaan u ON u.ElevID = e.ElevID Join instrument i ON u.instrumentID = i.InstrumentID "
        f"WHERE e.ElevID = {renter_id}")

    person = renter[0]

    output_instrument: list[dict] = []

    output_person: list[dict] = [{
        "Navn": f"{person['Fornavn']} {person['Etternavn']}",
        "Addresse": f"{person['Adresse']}"
    }]

    for row in renter:
        output_instrument.append({
            "Navn": row['Navn'],
            "Type": row['Type'],
            "Utlånsdato": row['Utlaansdato'],
            "Levert": row['Levert']
        })

    return [output_person, output_instrument]


if __name__ == "__main__":
    # print(send_query(f"SELECT * FROM elev"))
    print_result(send_query(f"SELECT * FROM elev"), title="Oppgave 1")

    print_nested_dict(instrument_lanerhistorikk(2))