import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

quotes = soup.find_all('span', class_='text')

authors = soup.find_all('small', class_='author')

for i in range(len(quotes)):
    print(quotes[i].text + " - " + authors[i].text)