#!python
print("content-type:text/html \r\n\r\n")
import cgi
import pymysql


#FieldStorage()
data=cgi.FieldStorage()
#getvalue()


br=data.getvalue('brand')
pr=data.getvalue('price')
inte=data.getvalue('internal')
ra=data.getvalue('ram')
wa=data.getvalue('warranty')
da=data.getvalue('date')



print("BRAND is :- ",br)
print("PRICE is :- ",pr)
print("INTERNAL MEMORY is :- ",inte)
print("RAM is :- ",ra)
print("WARRANTY is :- ",wa)
print("DATE is :- ",da)

servername="localhost"
username="root"
password=""
dbname="mob"

db=pymysql.connect(servername,username,password,dbname)

if db:
    print("<p>Success</p>")
    cur=db.cursor()
    query="insert into mob1(brand,price,internal,ram,warranty,date)values('{}','{}','{}','{}','{}','{}')".format(br,pr,inte,ra,wa,da)
    cur.execute(query)
    db.commit()
else :
    print("<p>NO</p>")
