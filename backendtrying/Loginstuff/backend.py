from flask import Flask, request
import sqlite3
import hashlib
from random import randint
from sanitizer import sanitize

app = Flask(__name__)
DATABASE = 'database.db'

def hash_password(password):
    # Hashen des Passworts mit SHA-256
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()

def getAllKeys():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT key FROM users")
    keys = cursor.fetchall()
    print(keys)
    return keys

def getUserByKey(key):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(f"SELECT username from users where key={key}")
    username = c.fetchall()[0]
    return username

def genKey(username):
    username = str(username)
    key = 0
    keys = getAllKeys()
    try:
        for char in username:
            if(key < 1000000000):
                key += randint(333, 33333)
                print(key)
        for k in keys():
            if(k == key):
                genKey(username)
    finally:
        return str(key)






@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    iban = request.form['iban']

    print(f'username: {username} password: {password} iban: {iban}')
    
    if(sanitize(username)): return "invalid username, please make sure you don't use any bad characters"
    if(sanitize(password)): return "invalid password, please make sure you don't use any bad characters"
    if(sanitize(iban)): return "invalid iban, please make sure you don't use any bad characters"


    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM users WHERE username = ?", (username,))
    amount = int(cursor.fetchone()[0])
    if(amount > 0):
        return 'user already exists, try login instead.'

    hashed_password = hash_password(password)
    hashed_iban = hash_password(iban)
    key = genKey(username)
    print(f"Register with: {username}, {password}, {key}, {hashed_iban}")
    cursor.execute("INSERT INTO users (username, password, isAdmin, key, iban) VALUES (?, ?, ?, ?, ?)",
                   (username, hashed_password, 0, key, hashed_iban))
    conn.commit()
    conn.close()
    print("success")

    return f'Registered successfully. Key:{key}'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    hashed_password = hash_password(password)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    print(f"Login with: {username}, {password}")

    cursor.execute("SELECT key FROM users WHERE username = ? AND password = ?",
                   (username, hashed_password))
    result = cursor.fetchone()
    conn.close()
    print("result? ", result)
    key = result[0];
    if (result):
        return f'Login successful key:{key}'
    else:
        return 'Login failed, please try again'




if __name__ == '__main__':
    app.run(debug=True)
