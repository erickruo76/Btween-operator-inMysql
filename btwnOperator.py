
import mysql.connector
#to use this library first instal thev'mysql' module installed, use the command below 
# pip install mysql-connector-python

mydb = mysql.connector.connect(
    host='localhost',
    user="root",
    password="",
    database="events_db"
)

cur = mydb.cursor()

get_data = "SELECT * FROM crud WHERE id BETWEEN 2 AND 3"

cur.execute(get_data)
data = cur.fetchall()

for i in data:
    print(i)

cur.close()
mydb.close()
