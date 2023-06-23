import requests
from bs4 import BeautifulSoup

resp = requests.get('https://oto.com.vn/mua-ban-xe')
soup = BeautifulSoup(resp.content, "html.parser")
links = soup.select(' .box-list-car > .item-car > .photo > a')
print(links)