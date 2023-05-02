from flask import Flask, request, jsonify
import os
import sqlite3
import random

app = Flask(__name__)

def db_connect():
    conn = sqlite3.connect('runtime.db')
    return conn

def db_close(conn):
    conn.commit()
    conn.close()

@app.route('/load_deck', methods=['POST'])
def load_deck():
    # get request parameters from JSON body
    deck_name = request.args.get('deck_name')
    player_name = request.args.get('player_name')
    os.system(f'echo {deck_name} {player_name} > .tmp.txt')

    # deck_name = "Phyrexian"
    # player_name = "simi"

    # connect to storage and runtime databases
    storage_conn = sqlite3.connect('storage.db')
    runtime_conn = sqlite3.connect('runtime.db')

    # retrieve the cards for the specified deck from the storage database
    storage_cursor = storage_conn.cursor()
    storage_cursor.execute(
        '''SELECT name, img, deck FROM cards WHERE deck = ?''', (deck_name,))
    cards = storage_cursor.fetchall()
    print(cards)

    # add the cards to the runtime database with the specified player name
    runtime_cursor = runtime_conn.cursor()
    runtime_cursor.execute(
        '''INSERT INTO players (name, deck) values (?, ?)''', (player_name, deck_name))
    for card in cards:
        runtime_cursor.execute('''INSERT INTO library (name, img, deck, controller) values (?, ?, ?, ?)''',
                               (card[0], card[1], card[2], player_name))

    # player_id = 0

    # rows = runtime_cursor.fetchall()
    # for row in rows:
    #     print(row)
    #     player_id = row[0]

    # for card in cards:
    #     print(card)
    #     card_name = card[0]
    #     amount = int(card[1])
    #     for i in range(amount):
    #         runtime_cursor.execute('''INSERT INTO {} (name, img_url, deck_name, player_name) VALUES (?, ?, ?, ?)'''.format(tablename),
    #                                 (card_name, card[3], 'deck_name', player_name))

    # commit changes and close connections
    os.system(f'del .tmp.txt')
    runtime_conn.commit()
    runtime_conn.close()
    storage_conn.close()

    try:
        # return success message
        return jsonify({'message': 'Deck loaded successfully.'})
    except:
        print("The response wasn't able to be send, doesn't matter if manual execute")

@app.route('/shuffle_library/<deck_name>')
def shuffle_library(deck_name):
    conn = db_connect()
    cur = conn.cursor()

    cur.execute(f"SELECT COUNT(*) FROM library WHERE deck_name = ?", (deck_name,))
    num_cards = cur.fetchone()[0]
    card_ids = list(range(1, num_cards+1))
    random.shuffle(card_ids)

    for i, card_id in enumerate(card_ids, 1):
        cur.execute(f"UPDATE library SET id = ? WHERE id = ? AND deck_name = ?", (i, card_id, deck_name))

    db_close(conn)

    return "Library shuffled"

@app.route('/draw_card/<deck_name>')
def draw_card(deck_name):
    conn = db_connect()
    cur = conn.cursor()

    cur.execute(f"SELECT id, name, img_url FROM library WHERE deck_name = ? ORDER BY id ASC LIMIT 1", (deck_name,))
    card = cur.fetchone()
    if card is not None:
        cur.execute(f"DELETE FROM library WHERE id = ?", (card[0],))
        cur.execute(f"INSERT INTO hand (name, img_url, deck_name, player_name) VALUES (?, ?, ?, ?)", (card[1], card[2], deck_name, player_name))

    db_close(conn)

    return "Card drawn"

@app.route('/cast_card/<player_name>/<card_name>')
def cast_card(player_name, card_name):
    conn = db_connect()
    cur = conn.cursor()

    cur.execute(f"SELECT id, name, img_url FROM hand WHERE deck_name = ? AND name = ?", (deck_name, card_name))
    card = cur.fetchone()
    if card is not None:
        cur.execute(f"DELETE FROM hand WHERE id = ? AND controller = ?", (card[0], ))
        cur.execute(f"INSERT INTO battlefields_{player_name} (name, img_url, deck_name, player_name) VALUES (?, ?, ?, ?)", (card[1], card[2], deck_name, player_name))

    db_close(conn)

    return "Card cast"

@app.route('/move/<from>/<to><card_name>')
def move_permanent(from_pos, to, card_name):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM ? where name=?", (from_pos, card_name))
    card = cur.fetchone()
    cur.execute(f'INSERT INTO ? VALUES (?,?,?,?,?)',(to, card[0],  card[1], card[2], card[3], card[4]))

    db_close(conn)
    return f"moved {card_name} from {from_pos} to {to}"

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


if __name__ == '__main__':
    app.run(debug=True)
