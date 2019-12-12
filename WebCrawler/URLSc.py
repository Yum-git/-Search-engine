import requests
from bs4 import BeautifulSoup

def URLSc(url):
    response = requests.get(url)
    urlget = BeautifulSoup(response.text, "html.parser")
    for i in urlget.find_all('a'):
        urlreturn = i.get('href')
        if 'false':
            URLSc(urlreturn)
        else:
            if urlreturn.startswith('http'):
                print(urlreturn)

if __name__ == "__main__":
    url = 'https://www.sejuku.net/blog/'
    URLSc(url)