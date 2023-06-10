import requests
from bs4 import BeautifulSoup

url = 'https://ridibooks.com/category/free-books/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

bookservices = soup.select('fig-1rl9mz1')
for no, book in enumerate(bookservices, 1):
    print(no, book.text.strip())
