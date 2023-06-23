import requests
from bs4 import BeautifulSoup

resp = requests.get('https://batdongsan24h.com.vn/bat-dong-san-ban-tai-viet-nam-s32113')
soup = BeautifulSoup(resp.content, "html.parser")

class_selectors = ['h3']
links = []

for selector in class_selectors:
    links.extend(soup.select('.clearfix > .item-re-list > .box-info-list > .box-title-item > {} > a'.format(selector)))

for link in links:
    print(link.get('href'))
