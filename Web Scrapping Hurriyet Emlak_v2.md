

```python
import requests
#r = requests.get("https://www.hurriyetemlak.com/konut-satilik/villa/listeleme?pageSize=10")

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,'html.parser')
results = soup.find_all("a", attrs={'class':'overlay-link'})



```


```python
I did not prefer to wrap results as string object in this project. 
But if you want to work on strings to wrap the features you can return results string by using str function.
```


```python
str_res = str(results[0])
str_res
```




    '<a class="overlay-link" data-ad-type="Turbo" data-age="10" data-date="23.11.2018" data-floor="Villa Katı" data-img-count="20" data-listing-id="77882-197" data-meter="800" data-owner="Emlakçıdan" data-price="6.750.000" data-room="8+2" data-seller-type="Kurumsal" data-user-id="2202929" href="/konut-satilik/ankara-golbasi-incek-emlakcidan-villa/detay/32201615" title="İNCEK\\u0027DE 3.5 DÖNÜM ARSA ÜZERİNDE MUHTEŞEM MALİKANE"></a>'




```python
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


```


```python
# Opening txt file from local saved file

import pandas as pd
import csv

file = "hurriyet.txt"

df = pd.read_csv(file, index_col=None)
df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>adres</th>
      <th>area-m2</th>
      <th>date</th>
      <th>owner</th>
      <th>price</th>
      <th>room</th>
      <th>seller</th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>/konut-satilik/canakkale-ezine-dalyan-emlakcid...</td>
      <td>120.0</td>
      <td>23.11.2018</td>
      <td>Emlakçıdan</td>
      <td>400.000</td>
      <td>4+1</td>
      <td>Kurumsal</td>
      <td>ÇANAKKALE EZİNE DALYAN MÜSTAKİL DUBLEX KUPON S...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>/konut-satilik/duzce-akcakoca-ayazli-emlakcida...</td>
      <td>200.0</td>
      <td>23.11.2018</td>
      <td>Emlakçıdan</td>
      <td>450.000</td>
      <td>4+2</td>
      <td>Kurumsal</td>
      <td>KARADENİZİN İNCİSİ AKÇAKOCADA MÜSTAKİL ÖZEL YA...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>https://www.hurriyetemlak.com/projeler/kaplanl...</td>
      <td>75.0</td>
      <td>12.11.2018</td>
      <td>İnşaat Firmasından</td>
      <td>280.000</td>
      <td>2+1</td>
      <td>Projeland</td>
      <td>Sena Life</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
        

```


```python
df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>adres</th>
      <th>area-m2</th>
      <th>date</th>
      <th>owner</th>
      <th>price</th>
      <th>room</th>
      <th>seller</th>
      <th>title</th>
      <th>şehir</th>
      <th>ilçe</th>
      <th>mahalle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>canakkale-ezine-dalyan</td>
      <td>120.0</td>
      <td>23.11.2018</td>
      <td>Emlakçıdan</td>
      <td>400.000</td>
      <td>4+1</td>
      <td>Kurumsal</td>
      <td>ÇANAKKALE EZİNE DALYAN MÜSTAKİL DUBLEX KUPON S...</td>
      <td>canakkale</td>
      <td>ezine</td>
      <td>dalyan</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>duzce-akcakoca-ayazli</td>
      <td>200.0</td>
      <td>23.11.2018</td>
      <td>Emlakçıdan</td>
      <td>450.000</td>
      <td>4+2</td>
      <td>Kurumsal</td>
      <td>KARADENİZİN İNCİSİ AKÇAKOCADA MÜSTAKİL ÖZEL YA...</td>
      <td>duzce</td>
      <td>akcakoca</td>
      <td>ayazli</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>https:--www.hurriyetemlak.com-projeler-kaplanl...</td>
      <td>75.0</td>
      <td>12.11.2018</td>
      <td>İnşaat Firmasından</td>
      <td>280.000</td>
      <td>2+1</td>
      <td>Projeland</td>
      <td>Sena Life</td>
      <td>https:</td>
      <td></td>
      <td>www.hurriyetemlak.com</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>istanbul-sariyer-bahcekoy-merkez</td>
      <td>2700.0</td>
      <td>23.11.2018</td>
      <td>Emlakçıdan</td>
      <td>10.650.000</td>
      <td>8+2</td>
      <td>Kurumsal</td>
      <td>Sarıyer Bahçeköy de Emsalsiz 8+2 2678 m2 Lüx S...</td>
      <td>istanbul</td>
      <td>sariyer</td>
      <td>bahcekoy</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>ankara-cankaya-mutlukent</td>
      <td>850.0</td>
      <td>23.11.2018</td>
      <td>Emlakçıdan</td>
      <td>7.500.000</td>
      <td>6+3</td>
      <td>Kurumsal</td>
      <td>ANGORA EVLERİ ULTRA LÜKS ÇOK BÜYÜK BAHÇELİ SAT...</td>
      <td>ankara</td>
      <td>cankaya</td>
      <td>mutlukent</td>
    </tr>
  </tbody>
</table>
</div>


