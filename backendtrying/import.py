import sqlite3
import requests
import sys
from sanitizer import sanitize

# function to parse a single line of the decklist file
def parse_card_line(prefix, card_line):
    card_line = card_line.strip()  # remove leading/trailing whitespace
    amount, name = card_line.split(prefix, 1)  # split line into amount and name
    return name, int(amount)

# function to add cards to a deck in the database
def add_cards(conn, deck, card_list):
    print(f'{deck}{card_list}')
    x = 0
    cardamount = 0
    cursor = conn.cursor()
    for card_name, card_amount in card_list:
        if(not sanitize(card_name)):
            print(f"{card_name} is an invalid cardname, please contact the developer.")
        x = x + 1
        try:
            for i in range(card_amount):
                response = requests.get('https://api.scryfall.com/cards/named', params={'exact': card_name})
                if response.ok:
                    card_data = response.json()
                    card_image_url = card_data['image_uris']['normal']
                    card_type = card_data['type_line']
                if(card_image_url != '' and len(card_image_url) > 0):
                    cursor.execute("""
                    INSERT INTO cards (name, img, deck, type)
                    VALUES (?, ?, ?, ?)
                """, (card_name, card_image_url, deck, card_type))
        except:
            try:
                zone = "Mainboard"
                for i in range(card_amount):
                    response = requests.get('https://api.scryfall.com/cards/named', params={'exact': card_name})
                    if response.ok:
                        card_data = response.json()
                        card_image_url = card_data['card_faces'][0]['image_uris']['normal']

                        print(card_image_url)
                    if(card_image_url != '' and len(card_image_url) > 0):
                        cursor.execute("""
                        INSERT INTO cards (name, img, deck, zone, type)
                        VALUES (?, ?, ?, ?, ?,)
                    """, (card_name, card_image_url, deck, zone, card_type))
            except:
                print("idk")
                # cursor.execute("""
                #     INSERT INTO cards (name, deck, type)
                #     VALUES (?, ?, ?)
                # """, (card_name, deck, card_type))
        cardamount += card_amount
        if(x % 10 == 0): print(f'{cardamount} cards imported; last card {card_name}')


    print(f'{cardamount} cards imported; last card {card_name}')
    print("Finished")
    if(cardamount > 90):
        commander = input("is this a commander deck? (Y/n)").lower()
        if(commander == 'y'):
          commander = input("what is the name of your commander? ")
          print("not implemented yet")

    conn.commit()

# function to add a new deck to the database
def add_deck(conn, deck_name):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO decks (name)
        VALUES (?)
    """, (deck_name,))
    deck_id = cursor.lastrowid
    conn.commit()
    return deck_id

# function to import a deck from a file
def import_deck(file_path, deck_name):
    conn = sqlite3.connect('storage.db')
    card_list = []
    prefix = " "
    # read each line from the file and add the cards to the list
    with open(file_path, 'r') as f:
        for line in f:
            if(line[1] == 'x'): prefix = "x "
            card_name, card_amount = parse_card_line(prefix, line)
            card_list.append((card_name, card_amount))

    add_cards(conn, deck_name, card_list)
    cursor = conn.cursor()
    cursor.execute("select * from cards")
    conn.commit()
    conn.close()
deckname = ''
if __name__ == '__main__':
    # deckname = input("Whats your Deckname? ")
    try:
        deckname = sys.argv[1]
    except:
        deckname = "Phyrexian"
        fullimport = True
        print(f"Invalid deck, trying defined alternative {deckname}.")

    import_deck(f'{deckname}.txt', f'{deckname}')
    if fullimport:
        requests.get(f'http://localhost:5000/load_deck?player_name={"somelazyplayer"}&deck_name={deckname}')