import json

# JSON-Daten zum Schreiben
data_to_write = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {'name': 'joh', 'passion': 'inventor'}
]

# Daten in eine Datei im line-delimited JSON-Format schreiben
with open('data.jsonl', 'w') as file:
    for item in data_to_write:
        json.dump(item, file)  # Schreibt ein JSON-Objekt pro Zeile
        file.write('\n')  # Fügt einen Zeilenumbruch hinzu

# JSON-Daten aus der Datei lesen
data_to_read = []
with open('data.jsonl', 'r') as file:
    for line in file:
        print(line)
        data = json.loads(line)  # Liest ein JSON-Objekt pro Zeile
        data_to_read.append(data)

# Ausgabe der gelesenen Daten
for item in data_to_read:
    print(item)
