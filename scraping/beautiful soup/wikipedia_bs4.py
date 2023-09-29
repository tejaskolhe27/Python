# import requests
# from bs4 import BeautifulSoup
# import re

# url="https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture"
# response=requests.get(url)

# html_soup=BeautifulSoup(response.text,'html.parser')


# movie_containers=html_soup.find_all('tr',style='background:#FAEB86')
# first=movie_containers[0]
# val=first.find("a",{"href":re.compile("film")}).get("href")



# newurl="https://en.wikipedia.org"+val
# newresponse = requests.get(newurl)

# newdata=BeautifulSoup(newresponse.text,"html.parser")
# movies=html_soup.find_all('tr',style='background:#FAEB86')

# title=[]
# directedby=[]
# releasedata=[]
# for movie in movies:
#     title.append(movie.a.text)
#     directed_by=director.get_text() for director in newdata.select("tr:string=re.select('Directed by') a[href*='/wiki/']")
#     directedby.append(directed_by)

# # for movie in movie_containers:
# #     title.append(movie.a.text)
# #     # for director in html_soup.select("tr:-soup-contains('Directed by') a[href*='/wiki/']::text"):
            
# #     #         director.get_text()
# #     #         directedby.append(director)
# #     directedby = [director.get_text() for director in html_soup.select("tr:contains('Directed by') a[href*='/wiki/']")]
    
    
# # print(title)
# print(directedby)
# # time.sleep(5)



import time
import requests
from bs4 import BeautifulSoup
import csv

start_url = 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture'

csv_file = open('movie_data.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.DictWriter(csv_file, fieldnames=['TITLE', 'DIRECTED BY', 'RELEASE DATE'])
csv_writer.writeheader()

response = requests.get(start_url)

soup = BeautifulSoup(response.text, 'html.parser')

movie_links = soup.select("tr[style='background:#FAEB86'] a[href*='film)']")

for link in movie_links:
        
      
        movie_url = 'https://en.wikipedia.org' + link['href']
        movie_response = requests.get(movie_url)
        movie_soup = BeautifulSoup(movie_response.text, 'html.parser')
        title = movie_soup.select_one("h1[id='firstHeading'] i").get_text()
        directed_by = [director.get_text() for director in movie_soup.select("tr:contains('Directed by') a[href*='/wiki/']")]
        release_dates = [date.get_text() for date in movie_soup.select("tr:contains('Release dates') li")]
        data = {
                'TITLE': title,
                'DIRECTED BY': directed_by,
                'RELEASE DATE': release_dates,
            }
        csv_writer.writerow(data)
        print(f"Scraped data for: {title}")
        time.sleep(2)

# Close the CSV file
csv_file.close()