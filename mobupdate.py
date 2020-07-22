#!python
print("content-type:text/html \r\n\r\n")

import cgi

data=cgi.FieldStorage()

rcid=data.getvalue('id')
br=data.getvalue('brand')
pr=data.getvalue('price')
inte=data.getvalue('internal')
ra=data.getvalue('ram')
wa=data.getvalue('warranty')
da=data.getvalue('date')
#print("<h3>{}</h3>".format(rcid))


servername="localhost"
username="root"
password=""
dbname="mob"

import pymysql

db=pymysql.connect(servername,username,password,dbname)

cur=db.cursor()

query="UPDATE mob1 SET brand='{}',price='{}',internal='{}',ram='{}',warranty='{}',date='{}' WHERE id={}".format(br,pr,inte,ra,wa,da,rcid)

try:
  cur.execute(query)
  db.commit()
  
except:
  db.rollback()
  print("Error in Query")

  