import requests
from bs4 import BeautifulSoup

def scrape_google_results(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 오류가 발생하면 예외를 발생시킴
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    results = soup.select(".tF2Cxc")  # 검색 결과 요소 선택
    
    for result in results:
        title = result.select_one(".DKV0Md").text  # 제목 선택
        link = result.select_one(".yuRUbf a")["href"]  # 링크 선택
        print(f"Title: {title}")
        print(f"Link: {link}")
        print()
        
# 크롤링 실행
query = "OpenAI"
scrape_google_results(query)
