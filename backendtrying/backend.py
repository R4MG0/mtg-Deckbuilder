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

async def sendData(data):
    async with websockets.connect("ws://localhost:8765") as websocket:
            await websocket.send(data)


@app.route('/move', methods=['POST'])
def read_post_param():
    # Get the value of the 'my_param' parameter from the POST request
    origin = request.form.get('from')
    newpos = request.form.get('to')
    cardId = request.form.get('cardId')
    info = f"{origin};{newpos};{cardId}"

    conn = db_connect()
    cur = conn.cursor()
    try:
        print(origin)
        # Try to fetch card to go sure it exists
        cmd = f"SELECT id, name, img, deck, controller, zone, attributes FROM {origin} WHERE id={cardId} LIMIT 1"
        print(cmd)
        # cur.execute(cmd)
        # cur.execute("""SELECT * FROM ? WHERE id = ?""", (origin, cardId,))
        # print('test')
        # card = cur.fetchall()
        cur.execute(f"SELECT * FROM {origin} WHERE id={cardId}")
        card = cur.fetchone()
        print(f"Cardname: {card[5]}")
        # return f'{card}, from {origin} to {newpos}'
    except:
        return "this card doesn't exist"
    # conn.execute("""DELETE FROM ? WHERE id=?""", (origin, cardId))
    cur.execute(f"DELETE FROM {origin} WHERE id={cardId}")
    print(f"DELETE FROM {origin} WHERE id = {cardId}")
    if (newpos != "phasedout"):
        print(newpos)
    # conn.execute(
    #     """INSERT INTO ? (name, img, deck, controller, zone, attributes) VALUES (?,?,?,?,?,?,)""", (newpos, card[1], card[2], card[3], card[4], card[5], card[6]))
    cur.execute(f"INSERT INTO {newpos} (name, img, deck, controller, zone, attributes) VALUES (?,?,?,?,?,?)", (card[1],card[2],card[3],card[4],card[5],card[6]))
    db_close(conn)
    #  Return a response
    try:
        # WS
        sendData(info)
    except:
        print(f"there was an error while sending data via websocket ({info})")
        return f'problem sending data {info}'

    return f'Moved card: {card[1]}|{info}'

@app.route('/changecontroller', methods=['POST'])
def changeController():
    # Requires the position of the card
    # the id of the card so there's no room
    # for error
    # and the new controller, which should be set
    position = request.form.get('position')
    cardId = request.form.get('cardId')
    controller = request.form.get('controller')
    info = f"{position};{cardId};{controller}"

    rc = db_connect()
    c = rc.cursor()

    c.execute(f"UPDATE {position} SET controller = '{controller}' WHERE id = {cardId}")
    print(f"UPDATE {position} SET controller='{controller}' WHERE id={cardId}")

    db_close(rc)
    return "success"


@app.route('/load_deck', methods=['GET'])
def load_deck():
    # get request parameters from JSON body
    deck_name = request.args.get('deck_name')
    player_name = request.args.get('player_name')
    os.system(f'echo {deck_name} {player_name} > .deck.txt')

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


@app.route('/shuffle', methods=['POST'])
def shuffle(deck):
    # return "not implemented yet"
    deck = request.form.get('deck')
    conn = db_connect()
    cur = conn.cursor()

    r = "first card: "
    cur.execute(f"SELECT name FROM library WHERE deck={deck} LIMIT 1")
    r += cur.fetchone()[1]
    # cur.execute(
    #     f"SELECT (*) FROM library WHERE deck = ?", (deck,))
    # num_cards = cur.fetchone()[0]
    # card_ids = list(range(1, num_cards+1))
    # random.shuffle(card_ids)

    # for i, card_id in enumerate(card_ids, 1):
    #     cur.execute(
    #         f"UPDATE library SET id = ? WHERE id = ? AND deck = ?", (i, card_id, deck))

    cur.execute(
        f"SELECT * FROM library WHERE deck = ?", (deck,))
    deck = []
    deck = cur.fetchall()

    deck.shuffle()
    r += ", last card: "
    r += deck[0]
    print(deck.size())



    db_close(conn)
    return r


@app.route('/draw_card/<deck>')
def draw_card():
    conn = db_connect()
    cur = conn.cursor()
    deck = request.form.get('deck')
    cur.execute(
        f"SELECT id, name, img FROM library WHERE deck = ? ORDER BY id ASC LIMIT 1", (deck,))
    card = cur.fetchone()
    if card is not None:
        cur.execute(f"DELETE FROM library WHERE id = ?", (card[0],))
        cur.execute(f"INSERT INTO hand (name, img, deck, controller) VALUES (?, ?, ?, ?)",
                    (card[1], card[2], card[3], card[4]))

    db_close(conn)

    return f"Card drawn: {card[1]}"




if __name__ == '__main__':
    app.run(debug=True)
