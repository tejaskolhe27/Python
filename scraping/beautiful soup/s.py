import requests
from bs4 import BeautifulSoup
import re

url="https://www.imdb.com/search/title/?release_date=2022-01-01,2023-12-31"
response=requests.get(url)
print(response.text)

html_soup=BeautifulSoup(response.text,'html.parser')
type(html_soup)
print(html_soup)

movie_containers=html_soup.find_all('div',class_='lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))

first_movie=movie_containers[0]
print(first_movie)

h3=first_movie.h3.find_all("a")
# print(first_movie.h3)
# print(first_movie.h3.a)
print(first_movie.h3.a.text)

s=first_movie.find('span',class_='lister-item-year text-muted unbold')
print(s.text)

#for rating
print(first_movie.strong.text)

#to add all movies to a list
names=[]
rating=[]
year=[]
for movie in movie_containers:
    names.append(movie.h3.a.text)
    r=movie.strong
    if r!=None:
        rating.append(movie.strong.text)
    else:
        rating.append("Null")
        
    s=movie.find('span',class_='lister-item-year text-muted unbold')
    year.append(s.text)
    
print(names)
print(rating)
print(year)


import pandas as pd
data={"NAME":names,"RATINGS":rating,"YEAR":year}
df1=pd.DataFrame(data)
print(df1)

df1.to_csv("imdb.csv")  