import mysql.connector

conn = mysql.connector.connect(user = 'root', password = 'uinndouzu7', host = 'localhost', database = 'websc')
cur = conn.cursor()

cur.execute("insert into maintable(title, accesscount, mainid) values('pythonなのだ', 500, 1);")
cur.execute("select * from maintable;")



for row in cur.fetchall():
    print(row[0], row[1], row[2], row[3])

cur.close()
conn.commit()
conn.close()




