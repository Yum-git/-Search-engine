import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import requests
from bs4 import BeautifulSoup

import time

import sys

import mysql.connector

conn = mysql.connector.connect(user = 'root', password = 'uinndouzu7', host = 'localhost', database = 'websc')
cur = conn.cursor()

def URLSc(url, count):
    if counter == 500:
        cur.close()
        conn.commit()
        conn.close()
        sys.exit(1)
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
    
    
    
    title = urlget.find('title').text
    print(count, title, url)
    cur.execute("insert into maintable(title, url, mainid) values(%s, %s, 1);", (title, url, ))
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
                if count == 0 or count == 1:
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
    url = 'https://www.nikkei.com/'
    URLSc(url, 0)
    cur.close()
    conn.commit()
    conn.close()