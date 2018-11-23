

```python
import requests
r = requests.get("https://www.hurriyetemlak.com/konut-satilik/villa/listeleme?pageSize=100")

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,'html.parser')
results = soup.find_all("a", attrs={'class':'overlay-link'})



```


```python
results[0:2]
```




    [<a class="overlay-link" data-ad-type="Turbo" data-age="0" data-date="22.11.2018" data-floor="Villa Katı" data-img-count="25" data-listing-id="81975-817" data-meter="155" data-owner="Emlakçıdan" data-price="525.000" data-room="3+1" data-seller-type="Kurumsal" data-user-id="1599464" href="/konut-satilik/balikesir-ayvalik-kucukkoy-emlakcidan-villa/detay/32270596" title="ULAŞ EMLAK\u0027TAN BAHÇELİ HAVUZLU SIFIR 3+1 SÜPER LÜKS VİLLA"></a>,
     <a class="overlay-link" data-ad-type="Turbo" data-age="1" data-date="22.11.2018" data-floor="Villa Katı" data-img-count="30" data-listing-id="77162-2800" data-meter="140" data-owner="Emlakçıdan" data-price="550.000" data-room="3+1" data-seller-type="Kurumsal" data-user-id="1458401" href="/konut-satilik/balikesir-edremit-gure-emlakcidan-villa/detay/32307751" title="GÜRE SSK MEVKİNDE SATILIK 3+1 LÜKS VİLLA DENİZE 300 METRE"></a>]




```python
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
      <td>/konut-satilik/balikesir-ayvalik-kucukkoy-emla...</td>
      <td>155</td>
      <td>22.11.2018</td>
      <td>Emlakçıdan</td>
      <td>525.000</td>
      <td>3+1</td>
      <td>Kurumsal</td>
      <td>ULAŞ EMLAK\u0027TAN BAHÇELİ HAVUZLU SIFIR 3+1 ...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>/konut-satilik/balikesir-edremit-gure-emlakcid...</td>
      <td>140</td>
      <td>22.11.2018</td>
      <td>Emlakçıdan</td>
      <td>550.000</td>
      <td>3+1</td>
      <td>Kurumsal</td>
      <td>GÜRE SSK MEVKİNDE SATILIK 3+1 LÜKS VİLLA DENİZ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.hurriyetemlak.com/projeler/kaplanl...</td>
      <td>75</td>
      <td>12.11.2018</td>
      <td>İnşaat Firmasından</td>
      <td>280.000</td>
      <td>2+1</td>
      <td>Projeland</td>
      <td>Sena Life</td>
    </tr>
    <tr>
      <th>3</th>
      <td>/konut-satilik/sakarya-sapanca-tepebasi-emlakc...</td>
      <td>225</td>
      <td>22.11.2018</td>
      <td>Emlakçıdan</td>
      <td>1.620.000</td>
      <td>6+1</td>
      <td>Kurumsal</td>
      <td>SAPANCA\u0027DA MÜSTAKİL HAVUZLU, GENİŞ BAHÇEL...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>/konut-satilik/duzce-akcakoca-osmaniye-emlakci...</td>
      <td>255</td>
      <td>22.11.2018</td>
      <td>Emlakçıdan</td>
      <td>750.000</td>
      <td>5+2</td>
      <td>Kurumsal</td>
      <td>AKÇAKOCA DA SATILIK LÜKS 5+2 VİLLA</td>
    </tr>
    <tr>
      <th>5</th>
      <td>/konut-satilik/sakarya-sapanca-tepebasi-emlakc...</td>
      <td>265</td>
      <td>22.11.2018</td>
      <td>Emlakçıdan</td>
      <td>2.200.000</td>
      <td>7+1</td>
      <td>Kurumsal</td>
      <td>\u0027\u0027 GÖL MANZARALI, MÜSTAKİL BAHÇELİ-H...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>/konut-satilik/balikesir-edremit-altinoluk-eml...</td>
      <td>190</td>
      <td>22.11.2018</td>
      <td>Emlakçıdan</td>
      <td>650.000</td>
      <td>4+1</td>
      <td>Kurumsal</td>
      <td>ALTINOLUK SATILIK GARAJLI 4+1 LÜKS VİLLALAR- D...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>https://www.hurriyetemlak.com/projeler/kaplanl...</td>
      <td>90</td>
      <td>12.11.2018</td>
      <td>İnşaat Firmasından</td>
      <td>320.000</td>
      <td>3+1</td>
      <td>Projeland</td>
      <td>Sena Life</td>
    </tr>
    <tr>
      <th>8</th>
      <td>/konut-satilik/istanbul-sariyer-zekeriyakoy-em...</td>
      <td>500</td>
      <td>22.11.2018</td>
      <td>Emlakçıdan</td>
      <td>5.350.000</td>
      <td>6+2</td>
      <td>Kurumsal</td>
      <td>NOKTA\u0027DAN ZEKERİYAKÖY\u0027DE ELİT SİTEDE...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>/konut-satilik/izmir-cigli-sasalli-merkez-emla...</td>
      <td>500</td>
      <td>22.11.2018</td>
      <td>Emlakçıdan</td>
      <td>2.850.000</td>
      <td>6+1</td>
      <td>Kurumsal</td>
      <td>Sasalı Yelken Konakların da 6+1, 500m2  Satıl...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>/konut-satilik/ankara-golbasi-karsiyaka-emlakc...</td>
      <td>220</td>
      <td>22.11.2018</td>
      <td>Emlakçıdan</td>
      <td>850.000</td>
      <td>4+1</td>
      <td>Bireysel</td>
      <td>GÖLBAŞI NESİBE AYDIN YANI 4+1 YENİ SİTEİÇİ VİL...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>/konut-satilik/ankara-cankaya-beytepe-emlakcid...</td>
      <td>250</td>
      <td>22.11.2018</td>
      <td>Emlakçıdan</td>
      <td>495.000</td>
      <td>5+1</td>
      <td>Kurumsal</td>
      <td>ACAR BEYTEPE SİT.GENİŞ BAHÇELİ ÖNÜ AÇIK TRIBLEKS</td>
    </tr>
    <tr>
      <th>12</th>
      <td>https://www.hurriyetemlak.com/projeler/cagri-y...</td>
      <td>105</td>
      <td>13.11.2018</td>
      <td>İnşaat Firmasından</td>
      <td>300.000</td>
      <td>2+1</td>
      <td>Projeland</td>
      <td>Kartepe Stone Suites</td>
    </tr>
    <tr>
      <th>13</th>
      <td>/konut-satilik/istanbul-sariyer-bahcekoy-merke...</td>
      <td>1100</td>
      <td>22.11.2018</td>
      <td>Emlakçıdan</td>
      <td>39.770.000</td>
      <td>6+2</td>
      <td>Kurumsal</td>
      <td>Bahçeköy SAKLI KORU\u0027 da VİP Kupon VİLLA</td>
    </tr>
    <tr>
      <th>14</th>
      <td>/konut-satilik/istanbul-sariyer-zekeriyakoy-em...</td>
      <td>300</td>
      <td>22.11.2018</td>
      <td>Emlakçıdan</td>
      <td>1.650.000</td>
      <td>4+2</td>
      <td>Kurumsal</td>
      <td>Havuzlu ve Guvenlikli sitede 300m2 Müstakil Vi...</td>
    </tr>
  </tbody>
</table>
</div>


