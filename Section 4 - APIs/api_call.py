import requests

base_url = "https://api.upcitemdb.com/prod/trial/lookup"

parameters = {'upc': '012993441012'}

response = requests.get(base_url, params=parameters)

print(response.url)