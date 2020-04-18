import requests

url = 'https://www.python.org/ftp/python/2.7.4/Python-2.7.4.tar.xz'
#get the file in binary format
r = requests.get(url)
with open("roshan-python-274.tar.xz","wb") as file:
    file.write(r.content)


