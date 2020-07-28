import requests
import json

base_url = "https://api.upcitemdb.com/prod/trial/lookup"

parameters = {'upc': '012993441012'}

response = requests.get(base_url, params=parameters)

print(response.url)

content = response.content
response_dict = json.loads(content)
print(response_dict)

iteminfo = response_dict['items'][0]
title = iteminfo['title']
brand = iteminfo['brand']

print("Title: " + title)
print("Brand: " + brand)