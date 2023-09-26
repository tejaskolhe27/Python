import requests
from bs4 import BeautifulSoup
import re

url="https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture"
response=requests.get(url)

html_soup=BeautifulSoup(response.text,'html.parser')


movie_containers=html_soup.find_all('tr',style='background:#FAEB86')
first=movie_containers[0]
val=first.find("a",{"href":re.compile("film")}).get("href")



newurl="https://en.wikipedia.org"+val
newresponse = requests.get(newurl)

newdata=BeautifulSoup(newresponse.text,"html.parser")
movies=html_soup.find_all('tr',style='background:#FAEB86')

title=[]
directedby=[]
releasedata=[]
for movie in movies:
    title.append(movie.a.text)
    directed_by=director.get_text() for director in newdata.select("tr:string=re.compile('Directed by') a[href*='/wiki/']")
    directedby.append(directed_by)

# for movie in movie_containers:
#     title.append(movie.a.text)
#     # for director in html_soup.select("tr:-soup-contains('Directed by') a[href*='/wiki/']::text"):
            
#     #         director.get_text()
#     #         directedby.append(director)
#     directedby = [director.get_text() for director in html_soup.select("tr:contains('Directed by') a[href*='/wiki/']")]
    
    
# print(title)
print(directedby)
# time.sleep(5)

