import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import requests
from bs4 import BeautifulSoup

import time

import sys

import mysql.connector

print('Mysql password please:')
passinput = input()
try:
    conn = mysql.connector.connect(user = 'root', password = passinput, host = 'localhost', database = 'websc')
except:
    print('passward is incorrect.')
    sys.exit(0)
cur = conn.cursor()

pageurl = []
def URLSc(url, count):
    global pageurl
    time.sleep(2)
    response = requests.get(url)
    urlget = BeautifulSoup(response.text, "html.parser")
    
    """
    TextGet = urlget
    for script in TextGet(["script", "style"]):
        script.decompose()
    text = TextGet.get_text()
    lines = [line.strip() for line in text.splitlines()]
    text = "\n".join(line for line in lines if line)
    with open('clone.txt', mode='a', encoding="utf-8_sig") as f:
        f.write(url + '\n\n' + text + '\n\n')
    """
    
    
    if url not in pageurl:
        pageurl.append(url)
        title = urlget.find('title').text
        print(count, title, url)
        cur.execute("insert into maintable(title, url, mainid) values(%s, %s, %s);", (title, url, 1))
        conn.commit()
        
    
    

    for i in urlget.find_all('a'):
        urlreturn = i.get('href')
        try:
            if type(urlreturn) == 'NoneType':
                continue
            elif urlreturn.startswith('http'):
                #print(count, ':', urlreturn)
                """
                with open('clone.txt', mode='a') as f:
                    f.write(urlreturn + '\n')
                """
                if count != 2:
                    URLSc(urlreturn, count + 1)
                else:
                    continue
            
        except AttributeError as e:
            print(e)
            """
            time.sleep(10)
            cur.close()
            conn.commit()
            conn.close()
            sys.exit(0)
            """
            
        """
        if type(urlreturn) == 'NoneType':
            continue
        elif urlreturn.startswith('http'):
            print(count, ':', urlreturn)
            with open('clone.txt', mode='a') as f:
                f.write(urlreturn + '\n')
            if count == 0:
                URLSc(urlreturn, 1)
            else:
                continue
        """
            


if __name__ == "__main__":
    url = 'https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8'
    URLSc(url, 0)
    cur.close()
    conn.commit()
    conn.close()