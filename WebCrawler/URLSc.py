import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import requests
from bs4 import BeautifulSoup

import time

def URLSc(url, count):
    time.sleep(3)
    response = requests.get(url)
    urlget = BeautifulSoup(response.text, "html.parser")
    for i in urlget.find_all('a'):
        urlreturn = i.get('href')
        if type(urlreturn) == 'NoneType':
            continue
        if urlreturn.startswith('http'):
            print(count, ':', urlreturn)
            
            if count == 0:
                URLSc(urlreturn, 1)
            else:
                continue
            


if __name__ == "__main__":
    url = 'https://www.nikkei.com/markets/kabu/'
    URLSc(url, 0)