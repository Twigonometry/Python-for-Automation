from bs4 import BeautifulSoup
import requests

url = "https://scrapingclub.com/exercise/list_basic/?page=1"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

def scrape_page(page_url, count):
    response = requests.get(page_url)

    page_soup = BeautifulSoup(response.text, 'lxml')

    items = page_soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for i in items:
        item_name = i.find('h4', class_='card-title').text.strip('\n')
        item_price = i.find('h5').text
        print('%s) Price: %s, Item Name: %s' % (count, item_price, item_name))
        count += 1

    return count

pages = soup.find('ul', class_="pagination")
urls = []
links = pages.find_all('a', class_="page-link")
for link in links:
    page_num = int(link.text) if link.text.isdigit() else None
    if page_num != None:
        x = link.get('href')
        urls.append("https://scrapingclub.com/exercise/list_basic/" + x)

count = 1

for url in urls:
    new_items = scrape_page(url, count)
    count = new_items