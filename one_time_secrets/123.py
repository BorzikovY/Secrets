import requests
response = requests.post('http://127.0.0.1:8000/generate/', json={'text': '...', 'secret_word': '...', 'time_of_death': 1, 'time_system': 'HOURS'})
print(response.json())
# response = requests.get('http://127.0.0.1:8000/admin/')
# print(response)