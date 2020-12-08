import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://keithgalli.github.io/web-scraping/example.html')

soup = bs(r.content)

print(soup.prettify())
