import requests
from bs4 import BeautifulSoup
import pandas as pd
import threading
from queue import Queue
import os

listCarLinks = []
baseUrl = 'https://batdongsan24h.com.vn/bat-dong-san-ban-tai-viet-nam-s32113/-1/-1/-1?page='

title = []
area = []
price = []
phone = []
ward = []
district = []
city = []
date = []
imageLink = []

dict_ = {'Title': title, 'Area': area, 'Price': price, 'Phone': phone, 'Ward': ward, 'District': district,
         'City': city, 'Date': date, 'ImageLink': imageLink}


def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded: {filename}")
    else:
        print(f"Failed to download image: {filename}")


def scrape_page(page_num):
    resp = requests.get(baseUrl + str(page_num))
    soup = BeautifulSoup(resp.content, "html.parser")

    houseTitle = soup.select('.clearfix > .item-re-list > .box-info-list > .box-title-item > h3 > a')
    for t in houseTitle:
        title.append(t.get_text())

    others = soup.select('.clearfix > .item-re-list > .box-info-list > .price-list > strong')

    for i in range(0, len(others) + 1 - 4, 4):
        area.append(others[i].get_text())
        price.append(others[i + 1].get_text())
        phone.append(others[i + 2].get_text())
        location = others[i + 3].get_text().split('-')
        ward.append(location[0].strip())
        if location[1].strip().lower().startswith("tp") or location[1].strip().lower() == 'hà nội':
            city.append(location[1].strip())
            district.append('')
        else:
            district.append(location[1].strip())
            if len(location) == 3:
                city.append(location[2].strip())
            else:
                city.append('')

    times = soup.select('.clearfix > .item-re-list > .box-info-list > .price-list > .pull-right')
    for time in times:
        date.append(time.get_text().strip())

    images = soup.select('.clearfix > .item-re-list > .box-img-thumb > a > img')
    for image in images:
        if image.get('src') == '/Content/images/pic-default.jpg':
            imageLink.append("NULL")
        else:
            imageLink.append(image.get('src'))


def worker():
    while True:
        page_num = queue.get()
        scrape_page(page_num)
        queue.task_done()


# Number of threads to use
num_threads = 4

# Create a queue to hold the page numbers
queue = Queue()

# Create and start worker threads
for _ in range(num_threads):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# Enqueue the page numbers to be scraped
for i in range(1, 20):
    queue.put(i)

# Wait for all tasks in the queue to be completed
queue.join()

df = pd.DataFrame(dict_)
df.to_csv('batdongsan.csv', encoding='utf-8')

# Create the 'images' folder if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Download and save each image
for i, link in enumerate(imageLink):
    if link != "NULL":
        filename = f"images/image{i+1}.jpg"  # Change the filename format if desired
        download_image(link, filename)
