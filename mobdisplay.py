#!python
print("content-type:text/html \r\n\r\n")
print("<h2>Records From Database<h2>")

start='''
    <table border=4>
        <tr>
            <td>Brand</td>
            <td>Price</td>
            <td>Internal</td>
            <td>Ram</td>
            <td>Warranty</td>
            <td>Date</td>
            <td>Edit</td>
            <td>View</td>
            <td>Delete</td>
        </tr>
'''
print(start)

import pymysql

servername="localhost"
username="root"
password=""
dbname="mob"

db=pymysql.connect(servername,username,password,dbname)

cur=db.cursor()

query="select * from mob1"
cur.execute(query)
data=cur.fetchall()

for row in data:
    print("<tr>")
    print("<td>{}</td>".format(row[1]))
    
    print("<td>{}</td>".format(row[2]))
    
    print("<td>{}</td>".format(row[3]))

    print("<td>{}</td>".format(row[4]))

    print("<td>{}</td>".format(row[5]))

    print("<td>{}</td>".format(row[6]))
    
    print("<td><a href='mobedit.py?id={}'>EDIT</td>".format(row[0]))
    
    print("<td><a href='mobview.py?id={}'>VIEW</td>".format(row[0]))
    
    print("<td><a href='mobdelete.py?id={}'>DELETE</td>".format(row[0]))

end='''
</table>
'''
print(end)
    