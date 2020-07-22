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

query="Delete from mob1 where id={}".format(rcid)
try:
    cur.execute(query)
    data=cur.fetchone()
    print("<h4>Data Deleted !! Check YOUR DataBase</h4>")
    db.commit()
except:
    print("<h4>problem iin query</h4>")
    db.rollback()