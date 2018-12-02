#acıklama acıklarımmmmmm
import pandas as pd
import requests
from bs4 import BeautifulSoup

price = []
date = []
area = []
owner = []
room = []
seller = []
adres = []
title = []

#Getting related info for 10 pages, each consists 50 house 
for i in range(10):
    r = requests.get("https://www.hurriyetemlak.com/konut-satilik/villa/listeleme?pageSize=50&page="+str(i))
    soup = BeautifulSoup(r.text,'html.parser')
    
    #Info related to house exists in "a" tag
    results = soup.find_all("a", attrs={'class':'overlay-link'})
    for tag in results :
        price.append(tag.get('data-price'))
        date.append(tag.get('data-date'))
        area.append(tag.get('data-meter'))
        owner.append(tag.get('data-owner'))
        room.append(tag.get('data-room'))
        seller.append(tag.get('data-seller-type'))
        adres.append(tag.get('href'))
        title.append(tag.get('title'))

    #creating a dictionary with title (keys) and the house info (values)
    records={"title": title, "price": price, "date":date, "area-m2": area, "owner":owner, "room": room, "seller": seller, "adres":adres, }

df = pd.DataFrame(records)
print (df)

df.to_csv("hurriyet.txt")
