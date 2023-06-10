import requests
from bs4 import BeautifulSoup

url = 'https://ridibooks.com/bestsellers/comic'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

bookservices = soup.select('.fig-yo8n1d')
for no, book in enumerate(bookservices, 1):
    print(no, book.text.strip())
