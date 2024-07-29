# Flights scraper
# Using Selenium and BeautifulSoup
import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/travel/flights?gl=US&hl=en-US'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)