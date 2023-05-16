import requests

# Basis-URL des Backends
base_url = 'http://localhost:5000/'

# Funktion zum Registrieren eines Benutzers
def register(username, password, iban):
    endpoint = 'register'
    url = base_url + endpoint
    data = {
        'username': username,
        'password': password,
        'iban': iban
    }
    response = requests.post(url, data=data)
    key = response.text.split(':')#[1]
    print(response.text)
    print(f" key: {key}")
    return key

# Funktion zum Einloggen eines Benutzers
def login(username, password):
    endpoint = 'login'
    url = base_url + endpoint
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(url, data=data)
    print(response.text)

# Funktion zum Erstellen eines Eintrags
def create_entry(image_path, number, subject, key):
    endpoint = 'create_entry'
    url = base_url + endpoint
    files = {'image': open(image_path, 'rb')}
    data = {
        'number': number,
        'subject': subject,
        'key': key
    }
    response = requests.post(url, files=files, data=data)
    key = response.text.split(':')#[1]
    print(response.text)
    print(f" key: {key}")

# Beispielaufrufe der Funktionen
key1 = register('JohnDoe', 'mypassword', 'DE1234567890')
key2 = register('JohnDoer', 'mypassword', 'DE1234567893')

login('JohnDoe', 'mypassword')
create_entry('illuminati.jpg', 123, 'Test Entry', key1)