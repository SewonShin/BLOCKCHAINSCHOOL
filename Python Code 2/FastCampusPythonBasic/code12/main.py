# import requests
# from bs4 import BeautifulSoup as bs

# URL = "https://www.fastcampus.co.kr/dev_online_introp/"

# rq = requests.get(URL)
# soup = bs(rq.content, 'html.parser')
# print(soup)


import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.fastcampus.co.kr/dev_online_introp/"

# div.vc_toggle_content > ul > li
rq = requests.get(URL)
soup = bs(rq.content, 'html.parser')

# (class, id, ...), attr = {key : value, ...}
li_list = soup.find_all('div', class_ = 'vc_toggle_content')
# li_list -> 모든 강의 내용, 강의 과제 
for li in li_list:
    ul = li.select('ul > li')
    for l in ul:
        print(l.get_text())
















