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
                  if "April 6, 2013" in version.select(".release-date")[0].get_text():
                      print("this is the one")
                      print(version.select(".release-number")[0].get_text().split(" ")[1])
print("The file you want to download is: Python 2.7.4 ")
urllib.request.urlretrieve("https://www.python.org/ftp/python/2.7.4/Python-2.7.4.tar.xz")