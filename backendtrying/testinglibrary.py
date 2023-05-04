import requests

# Define the API endpoint
url = 'http://localhost:5000/library'


def shuffle():
    response = requests.get('http://localhost:5000/shuffle_library/Phyrexian')
    print(response.text)

def draw():
    response = requests.get('http://localhost:5000/draw_card/Phyrexian')
    print(response.text)
# Print the response
# shuffle()
draw()
