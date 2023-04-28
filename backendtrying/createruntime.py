import sqlite3



# Connect to the database
conn = sqlite3.connect('runtime.db')


conn.execute('''DROP TABLE IF EXISTS players''')
conn.execute('''DROP TABLE IF EXISTS hand''')
conn.execute('''DROP TABLE IF EXISTS library''')
conn.execute('''DROP TABLE IF EXISTS graveyard''')
conn.execute('''DROP TABLE IF EXISTS battlefield''')
conn.execute('''DROP TABLE IF EXISTS exile''')
conn.execute('''DROP TABLE IF EXISTS phasedout''')


# Create the tables
conn.execute('''CREATE TABLE players
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             deck TEXT NOT NULL)''')
conn.execute('''CREATE TABLE hand
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             img TEXT NOT NULL,
             deck TEXT NOT NULL,
             controller TEXT NOT NULL)''')

conn.execute('''CREATE TABLE library
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             img TEXT NOT NULL,
             deck TEXT NOT NULL,
             controller TEXT NOT NULL)''')

conn.execute('''CREATE TABLE graveyard
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             img TEXT NOT NULL,
             deck TEXT NOT NULL,
             controller TEXT NOT NULL)''')

conn.execute('''CREATE TABLE battlefield
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             img TEXT NOT NULL,
             deck TEXT NOT NULL,
             controller TEXT NOT NULL)''')

conn.execute('''CREATE TABLE exile
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             img TEXT NOT NULL,
             deck TEXT NOT NULL,
             controller TEXT NOT NULL)''')

conn.execute('''CREATE TABLE phasedout
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             img TEXT NOT NULL,
             deck TEXT NOT NULL,
             controller TEXT NOT NULL)''')


# Commit changes and close the connection
conn.commit()
conn.close()
