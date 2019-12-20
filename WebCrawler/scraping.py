import requests
from bs4 import BeautifulSoup
 
url = "https://www.nikkei.com/markets/kabu/"
 
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


print(soup.title.string)
HyperURLList = []
for i in soup.find_all('a'):
    urlis = i.get("href")
    if urlis.startswith('http'):
        HyperURLList.append(urlis)
        

for i in HyperURLList:
    print(i)
        