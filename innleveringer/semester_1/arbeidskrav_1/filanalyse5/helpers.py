import csv

def read_csv_and_validate(filename):
    validated_data = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row_num, row in enumerate(reader, 2):
                if not all([row['Fornavn'], row['Etternavn'], row['Boktittel'],
                            row['Sjanger'], row['Lånedato'], row['Låneperiode'],
                            row['Forlenget'], row['Tilbakelevert']]):
                    print(f"Advarsel: Rad {row_num} mangler data og blir ignorert")
                    continue

                # Valider og konverter datatyper
                try:
                    validated_row = {
                        'Fornavn': row['Fornavn'].strip(),
                        'Etternavn': row['Etternavn'].strip(),
                        'Boktittel': row['Boktittel'].strip(),
                        'Sjanger': row['Sjanger'].strip(),
                        'Lånedato': row['Lånedato'].strip(),
                        'Låneperiode': int(row['Låneperiode']),
                        'Forlenget': 0 if row['Forlenget'].strip().lower() == 'abc' else int(row['Forlenget']),
                        'Tilbakelevert': row['Tilbakelevert'].strip()
                    }

                    validated_data.append(validated_row)

                except ValueError as e:
                    print(f"Advarsel: Rad {row_num} har ugyldige data: {e}. Raden blir ignorert.")
                    continue

    except FileNotFoundError:
        print(f"Feil: Filen '{filename}' ble ikke funnet.")
        return []
    except Exception as e:
        print(f"Feil ved lesing av fil: {e}")
        return []

    return validated_data