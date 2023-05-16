import sqlite3

# Datenbankdatei erstellen und Verbindung herstellen
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("DROP TABLE IF EXISTS entries")

# Tabelle für Benutzer erstellen
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        key INTEGER,
        isAdmin INTEGER,
        iban TEXT
    )
''')

# Tabelle für Einträge erstellen
cursor.execute('''
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        image BLOB,
        number INTEGER,
        subject TEXT,
        username TEXT
    )
''')

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()
