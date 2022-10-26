import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

# print(soup.prettify)
a = soup.find('tbody', class_='lister-list')
b = a.find_all('tr')

movie_list = []

for i in b:
  movie_name = i.find('td', class_='titleColumn').a.text
  dir_actor = i.find('td', class_='titleColumn').a['title']
  index_dir = i.find('td', class_='titleColumn').a['title'].find('dir')
  dir_name = dir_actor[:index_dir+5].replace('(dir.)', '')
  act_name = dir_actor[index_dir+6:]
  rating = i.find('td', class_="ratingColumn imdbRating").strong.text
  movie = {
      'movie_name':movie_name, 
      'director':dir_name,
      'actor':act_name,
      'rating':rating
  }
  movie_list.append(movie)
