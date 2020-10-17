import requests
from requests.exceptions import HTTPError


def print_json(json):
    for key, value in json.items():
        print(f'{key} : {value}')

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')
        json = response.json()
        print_json(json)

