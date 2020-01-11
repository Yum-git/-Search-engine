import mysql.connector
import sys
print('Mysql password please:')
passinput = input()
try:
    conn = mysql.connector.connect(user = 'root', password = passinput, host = 'localhost', database = 'websc')
except:
    print('passward is incorrect.')
    sys.exit(0)
    
cur = conn.cursor()

cur.execute("insert into maintable(title, accesscount, mainid) values('pythonなのだ', 500, 1);")
cur.execute("select * from maintable;")



for row in cur.fetchall():
    print(row[0], row[1], row[2], row[3])

cur.close()
conn.commit()
conn.close()




