import requests
from bs4 import BeautifulSoup
import urllib

result = requests.get('https://python.org/downloads')
src = result.content
soup = BeautifulSoup(src,'html.parser')
all_versions = soup.select('.list-row-container li')

for version in all_versions:
    for i in version.select(".release-date"):
              print(i.get_text())
              for i in version.select(".release-number"):
                  print(i.get_text())
                  for i in version.find_all('a',class_ ="release-download"):
                      print(i.get("href"))
                        


                   

                                 



        
            

        