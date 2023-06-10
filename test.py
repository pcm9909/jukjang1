import requests
from bs4 import BeautifulSoup

url = 'https://product.kyobobook.co.kr/bestseller/online?period=001'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

bookservices = soup.select('.prod_name')
for no, book in enumerate(bookservices, 1):
    print(no, book.text.strip())
