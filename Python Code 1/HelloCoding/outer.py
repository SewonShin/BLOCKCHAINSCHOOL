from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://m.stock.naver.com/marketindex/index.nhn")
soup = BeautifulSoup(target, "html.parser")

for tag in soup.select(".data_lst li"):
    print(tag.select_one(".value").string)
    print(tag.select_one(".bling").string)