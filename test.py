import requests
from bs4 import BeautifulSoup

url = 'https://ridibooks.com/category/new-releases/2200'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

response = requests.get(url, headers=headers)
response.raise_for_status()  # 오류가 발생하면 예외를 발생시킴

soup = BeautifulSoup(response.text, 'html.parser')

bookservices = soup.select('.title_text')
for no, book in enumerate(bookservices, 1):
    print(no, book.text.strip())
