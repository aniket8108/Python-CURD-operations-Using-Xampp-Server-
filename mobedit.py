#!python
print("content-type:text/html \r\n\r\n")

import cgi
data=cgi.FieldStorage()
rcid=data.getvalue('id')
#print("<h3>{}</h3>".format(rcid))

#retrive the record from database

import pymysql

servername="localhost"
username="root"
password=""
dbname="mob"

db=pymysql.connect(servername,username,password,dbname)

cur=db.cursor()

query="SELECT * FROM mob1 WHERE id={}".format(rcid)

cur.execute(query)

row=cur.fetchone()

content='''
<html>
   <body><form method="POST" action="mobupdate.py">
            <table>
                <tr>
                    <td>ID:</td>
                    <td><input type="text" name="id" value="{}"></td>
                </tr>
                
                <tr>
                    <td>BRAND</td>
                    <td><input type="text" name="brand" value="{}"></td>
                <tr>

                <tr>
                    <td>PRICE</td>
                    <td><input type="text" name="price" value="{}"></td>
                <tr>
                
                
                <tr>
                    <td>INTERNAL</td>
                    <td><input type="text" name="internal" value="{}"></td>
                </tr>

                <tr>
                    <td>RAM</td>
                    <td><input type="text" name="ram" value="{}"></td>
                </tr>
                
                <tr>
                    <td>WARRANTY</td>
                    <td><input type="text" name="warranty" value="{}"></td>
                </tr>

                <tr>
                    <td>DATE OF PURCHASE:- </td>
                    <td><input type="date" name="date" value="{}"></td>
                </tr>

                


                <tr>
                    <td><input type="submit" name="update" value="UPDATE"></td>
                </tr>

            </table>
        </form>
    </body>
</html>

'''.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6])


print(content)