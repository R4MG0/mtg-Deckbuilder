from flask import Flask

import sqlite3
import random

app = Flask(__name__)

def db_connect():
    conn = sqlite3.connect('runtime.db')
    return conn

def db_close(conn):
    conn.commit()
    conn.close()

@app.route('/shuffle_library/<player_name>/<deck_name>')
def shuffle_library(player_name, deck_name):
    conn = db_connect()
    cur = conn.cursor()

    cur.execute(f"SELECT COUNT(*) FROM library_{player_name} WHERE deck_name = ?", (deck_name,))
    num_cards = cur.fetchone()[0]
    card_ids = list(range(1, num_cards+1))
    random.shuffle(card_ids)

    for i, card_id in enumerate(card_ids, 1):
        cur.execute(f"UPDATE library_{player_name} SET id = ? WHERE id = ? AND deck_name = ?", (i, card_id, deck_name))

    db_close(conn)

    return "Library shuffled"

@app.route('/draw_card/<player_name>/<deck_name>')
def draw_card(player_name, deck_name):
    conn = db_connect()
    cur = conn.cursor()

    cur.execute(f"SELECT id, name, img_url FROM library_{player_name} WHERE deck_name = ? ORDER BY id ASC LIMIT 1", (deck_name,))
    card = cur.fetchone()
    if card is not None:
        cur.execute(f"DELETE FROM library_{player_name} WHERE id = ?", (card[0],))
        cur.execute(f"INSERT INTO hand_{player_name} (name, img_url, deck_name, player_name) VALUES (?, ?, ?, ?)", (card[1], card[2], deck_name, player_name))

    db_close(conn)

    return "Card drawn"

@app.route('/cast_card/<player_name>/<deck_name>/<card_name>')
def cast_card(player_name, deck_name, card_name):
    conn = db_connect()
    cur = conn.cursor()

    cur.execute(f"SELECT id, name, img_url FROM hand_{player_name} WHERE deck_name = ? AND name = ?", (deck_name, card_name))
    card = cur.fetchone()
    if card is not None:
        cur.execute(f"DELETE FROM hand_{player_name} WHERE id = ?", (card[0],))
        cur.execute(f"INSERT INTO battlefields_{player_name} (name, img_url, deck_name, player_name) VALUES (?, ?, ?, ?)", (card[1], card[2], deck_name, player_name))

    db_close(conn)

    return "Card cast"

@app.route('/destroy_permanent/<player_name>/<deck_name>/<card_name>')
def destroy_permanent(player_name, deck_name, card_name):
    conn = db_connect()
    cur = conn.cursor()

    cur.execute(f"SELECT id, name, img_url FROM battlefields_{player_name} WHERE deck_name = ? AND name = ?", (deck_name, card_name))
    card = cur.fetchone()
    if card is not None:
        cur.execute(f"DELETE FROM battlefields_{player_name} WHERE id = ?", (card[0],))
        cur.execute(f"INSERT INTO graveyards_{player_name} (name, img_url, deck_name, player_name) VALUES (?, ?, ?, ?)", (card[1], card[2], deck_name, player_name))

    db_close(conn)

    return "Permanent destroyed"

@app.route('/exile_card/<player_name>/<card_id>')
def exile_card(player_name, card_id):
    conn = sqlite3.connect('runtime.db')
    c = conn.cursor()

    # Get the card from the specified table based on the card_id and player_name
    c.execute(f"SELECT * FROM hand_{player_name} WHERE id={card_id}")
    card_data = c.fetchone()

    # If the card wasn't found in the player's hand, check their battlefield
    if not card_data:
        c.execute(f"SELECT * FROM battlefields_{player_name} WHERE id={card_id}")
        card_data = c.fetchone()

    # If the card wasn't found in the player's hand or battlefield, check their library
    if not card_data:
        c.execute(f"SELECT * FROM graveyards_{player_name} WHERE id={card_id}")
        card_data = c.fetchone()

    # If the card was found, remove it from its table and insert it into the exile
    if card_data:
        card_name = card_data[1]
        img_url = card_data[2]
        deck_name = card_data[3]
        c.execute(f"DELETE FROM hand_{player_name} WHERE id={card_id}")
        c.execute(f"DELETE FROM battlefields_{player_name} WHERE id={card_id}")
        c.execute(f"DELETE FROM graveyards_{player_name} WHERE id={card_id}")
        c.execute(f"INSERT INTO exiles_{player_name} (name, img_url, deck_name, player_name) VALUES ('{card_name}', '{img_url}', '{deck_name}', '{player_name}')")
        conn.commit()
        conn.close()
        return f"{card_name} was exiled."
    else:
        conn.close()
        return "Card not found in hand, battlefield, or graveyard."
