import requests
from bs4 import BeautifulSoup
import re

url="https://www.imdb.com/search/title/?release_date=2022-01-01,2023-12-31"
response=requests.get(url)


html_soup=BeautifulSoup(response.text,'html.parser')


movie_containers=html_soup.find_all('div',class_='lister-item mode-advanced')

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








    