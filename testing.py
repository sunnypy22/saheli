import requests
from bs4 import BeautifulSoup
import urllib.request

URL = "https://www.ebay.co.uk/itm/401299519601?hash=item5d6f50b871:g:iQAAAOSwXYtYy7de"
page = requests.get(URL)

soup = BeautifulSoup(page.text, "html.parser")
div = soup.find_all('div', {'id': 'CenterPanelInternal'})
images = []
title = []
for image in div:
    img = image.find_all('img', {'id': 'icImg'})
    for j in img:
        img = j.get('src')
        imgURL = img
        images.append(imgURL)
        urllib.request.urlretrieve(imgURL, "D:/local-filename.jpg")

for k in div:
    divu = k.find_all('div', {'id': 'LeftSummaryPanel'})
    h1 = k.find('h1', {'id': 'itemTitle'})
    final_title = h1.text.strip()
    title.append(final_title)

import csv
input_variable = [
    ['Title'],
    [title]
]
with open ('Example.csv','w',newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ')
    my_writer.writerows(input_variable)