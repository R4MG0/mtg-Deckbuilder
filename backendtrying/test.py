import requests

url = 'http://localhost:5000/move'


# MOVE TEST

# Define the POST data
data = {'from': 'library',
        'to': 'battlefield',
        'cardId': 2}

# Send the POST request
response = requests.post(url, data=data)

# Print the response
print(f"Success if data here: {response.text}")

# Change Controller Test

url = 'http://localhost:5000/changecontroller'

# Define the POST data
data = {'position': 'battlefield',
        'controller': 'monoblueplayer',
        'cardId': 1}

# Send the POST request
response = requests.post(url, data=data)

# Print the response
print(response.text)

# Shuffle library test

url = 'http://localhost:5000/shuffle'

data = {'deck': 'Phyrexian'}

resp = requests.post(url, data=data)
print(resp.text)
