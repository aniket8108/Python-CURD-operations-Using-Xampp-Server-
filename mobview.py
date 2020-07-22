#!python
print("content-type:text/html \r\n\r\n")
print("<h2>Records From Database<h2>")
import cgi
data=cgi.FieldStorage()
rcid=data.getvalue('id')

#print("<h4>{}</h4>".format(rcid))

import pymysql

servername="localhost"
username="root"
password=""
dbname="mob"

db=pymysql.connect(servername,username,password,dbname)

cur=db.cursor()

query="select * from mob1 where id={}".format(rcid)
try:
    cur.execute(query)
    data=cur.fetchone()
    print("BRAND :- {}<br>".format(data[1]))
    print("PRICE :- {}<br>".format(data[2]))
    print("INTERNAL :- {}<br>".format(data[3]))
    print("RAM :- {}<br>".format(data[4]))
    print("WARRANTY :- {}<br>".format(data[5]))
    print("DATE :- {}<br>".format(data[6]))

    db.commit()
except:
    print("<h4>problem iin query</h4>")
    db.rollback()