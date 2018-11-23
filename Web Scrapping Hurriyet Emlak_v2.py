
# coding: utf-8

# In[4]:


import requests
#r = requests.get("https://www.hurriyetemlak.com/konut-satilik/villa/listeleme?pageSize=10")

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,'html.parser')
results = soup.find_all("a", attrs={'class':'overlay-link'})




# In[ ]:


I did not prefer to wrap results as string object in this project. 
But if you want to work on strings to wrap the features you can return results string by using str function.


# In[7]:


str_res = str(results[0])
str_res


# In[153]:


import requests
#r = requests.get("https://www.hurriyetemlak.com/konut-satilik/villa/listeleme?pageSize=100")

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



# In[154]:


# Opening txt file from local saved file

import pandas as pd
import csv

file = "hurriyet.txt"

df = pd.read_csv(file, index_col=None)
df.head(3)


# In[155]:


#here I created 3 different columns[şehir, ilçe, mahalle from adres column.]

for i in range(0,len(df.iloc[:,1])):
    try:
        df.iloc[i,1] = "-".join(df.iloc[i,1].replace("/konut-satilik/","").replace("-emlakcidan-villa/detay","").replace("-sahibinden-villa/detay","").split("/"))
        df.iloc[i,1] = (str(df.iloc[i,1]))[0:-9]
        adres_list = (df.iloc[i,1].split("-"))
        df.loc[i,"şehir"]= adres_list[0]
        df.loc[i,"ilçe"]= adres_list[1]
        df.loc[i,"mahalle"]= adres_list[2]
    except:
        pass
        


# In[156]:


df.head(5)

