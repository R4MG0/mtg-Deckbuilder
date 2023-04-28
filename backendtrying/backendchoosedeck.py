from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/example', methods=['GET'])
def handle_example():
    name = request.args.get('name')
    return f'Hello, {name}!'

@app.route('/load_deck', methods=['GET'])
def load_deck():
    # get request parameters from JSON body
    deck_name = request.args.get('deck_name')
    player_name = request.args.get('player_name')

    # deck_name = "Phyrexian"
    # player_name = "simi"

    # connect to storage and runtime databases
    storage_conn = sqlite3.connect('storage.db')
    runtime_conn = sqlite3.connect('runtime.db')

    # retrieve the cards for the specified deck from the storage database
    storage_cursor = storage_conn.cursor()
    storage_cursor.execute('''SELECT name, amount, img_url, deck_name FROM cards WHERE deck_name = ?''', (deck_name,))
    cards = storage_cursor.fetchall()

    # add the cards to the runtime database with the specified player name
    runtime_cursor = runtime_conn.cursor()
    runtime_cursor.execute('''INSERT INTO players (name, deck_name) values (?, ?)''', (player_name, deck_name))
    print("Should be player there")
    runtime_cursor.execute('''SELECT id FROM players WHERE name = ?''', (player_name,))
    
    player_id = 0

    rows = runtime_cursor.fetchall()
    for row in rows:
        print(row)
        player_id = row[0]

    tablename = 'library_player' + str(player_id)
    for card in cards:
        print(card)
        card_name = card[0]
        amount = int(card[1])
        for i in range(amount):
            runtime_cursor.execute('''INSERT INTO {} (name, img_url, deck_name, player_name) VALUES (?, ?, ?, ?)'''.format(tablename),
                                    (card_name, card[3], 'deck_name', player_name))

    # commit changes and close connections
    runtime_conn.commit()
    runtime_conn.close()
    storage_conn.close()

    # return success message
    return jsonify({'message': 'Deck loaded successfully.'})
# load_deck()
if __name__ == '__main__':
    app.run(debug=True)