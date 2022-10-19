import pandas as pd
from bs4 import BeautifulSoup
import requests

# url = 'https://-----------------------------.com/collections/shop-all'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
name_price = soup.find_all('div',class_="grid-product__meta")

data = []

for i in name_price:
  product_name = i.find(class_='grid-product__title').text
  product_price = i.find(class_ ='grid-product__price').text.strip()
  product = {
      'product_name': product_name,
      'product_price': product_price
  }
  data.append(product)

df = pd.DataFrame(data)
df.to_csv('organic_body_products.csv', index=False)
