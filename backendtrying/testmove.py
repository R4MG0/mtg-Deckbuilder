import requests

# Define the API endpoint
url = 'http://localhost:5000/move'

# Define the POST data
data = {'from': 'library',
        'to': 'graveyard',
        'cardId': 2}

# Send the POST request
response = requests.post(url, data=data)

# Print the response
print(response.text)
