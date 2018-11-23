
# coding: utf-8

# In[140]:


import requests
r = requests.get("https://www.hurriyetemlak.com/konut-satilik/villa/listeleme?pageSize=100")

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,'html.parser')
results = soup.find_all("a", attrs={'class':'overlay-link'})




# In[143]:


results[0:2]


# In[150]:


import requests
r = requests.get("https://www.hurriyetemlak.com/konut-satilik/villa/listeleme?pageSize=100")

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,'html.parser')
results = soup.find_all("a", attrs={'class':'overlay-link'})


from bs4 import BeautifulSoup
price = []
date = []
area = []
owner = []
room = []
seller = []
adres = []
title = []
for tag in results :
    price.append(tag.get('data-price'))
    date.append(tag.get('data-date'))
    area.append(tag.get('data-meter'))
    owner.append(tag.get('data-owner'))
    room.append(tag.get('data-room'))
    seller.append(tag.get('data-seller-type'))
    adres.append(tag.get('href'))
    title.append(tag.get('title'))

records={"title": title, "price": price, "date":date, "area-m2": area, "owner":owner, "room": room, "seller": seller, "adres":adres, }

import pandas as pd

df = pd.DataFrame(records)
df.head(15)

df.to_csv("hurriyet.txt")

df.head(15)

