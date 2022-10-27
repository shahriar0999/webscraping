import pandas as pd
import requests 
from bs4 import BeautifulSoup

books = []

for n in range(1,26):
  url = f'https://www.rokomari.com/book/category/13/comics-graphic-novels?ref=home_cat13&page={n}'
  r = requests.get(url)

  soup = BeautifulSoup(r.text, 'html.parser')
  comic = soup.find_all('div', class_='col-4 col-xl-3')

  for i in comic:
    try:
      title = i.find('p', class_='book-title').text
      author = i.find('p', class_='book-author').text
      instock = i.find('p', class_='book-status text-capitalize').text
      original_price = i.find('strike', class_='original-price pl-2').text
      discount_price = i.find('p', class_='book-price').span.text
    except:
      print()
    book = {
        'book_name':title,
        'author_name':author,
        'original_price':original_price,
        'discount_price':discount_price,
        'instock': instock
    }
    books.append(book)
