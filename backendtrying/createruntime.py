import sqlite3



# Connect to the database
conn = sqlite3.connect('runtime.db')


conn.execute('''DROP TABLE IF EXISTS players''')
conn.execute('''DROP TABLE IF EXISTS hand_player1''')
conn.execute('''DROP TABLE IF EXISTS hand_player2''')
conn.execute('''DROP TABLE IF EXISTS library_player1''')
conn.execute('''DROP TABLE IF EXISTS library_player2''')
conn.execute('''DROP TABLE IF EXISTS graveyards_player1''')
conn.execute('''DROP TABLE IF EXISTS graveyards_player2''')
conn.execute('''DROP TABLE IF EXISTS battlefields_player1''')
conn.execute('''DROP TABLE IF EXISTS battlefields_player2''')
conn.execute('''DROP TABLE IF EXISTS exiles_player1''')
conn.execute('''DROP TABLE IF EXISTS exiles_player2''')


# Create the tables
conn.execute('''CREATE TABLE players
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             deck_name TEXT NOT NULL)''')
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

conn.execute('''CREATE TABLE phasedout
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



# Commit changes and close the connection
conn.commit()
conn.close()
