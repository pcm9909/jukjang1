import requests
from bs4 import BeautifulSoup

url = 'https://ridibooks.com/category/new-releases/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

booktitles = ['li.fig-ko232:nth-child({}) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)'.format(i) for i in range(1,33)]
for booktitle in booktitles:
    print(soup.select(booktitle)[0].get_text())
