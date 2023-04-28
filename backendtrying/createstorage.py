import sqlite3

# Create the database and the tables

def create_database():
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS Decks;')
    # Create the Decks table
    c.execute('''CREATE TABLE IF NOT EXISTS Decks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 description TEXT)''')

    # Create the Cards table
    c.execute('DROP TABLE IF EXISTS Cards;')

    c.execute('''CREATE TABLE IF NOT EXISTS Cards
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 img TEXT,
                 deck TEXT,
                 type TEXT,
                 controller TEXT)''')

    # Save the changes and close the connection
    conn.commit()
    conn.close()
create_database()