print("Hello!")
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="1234", database="patils")

mycorsor = mydb.cursor()

mycorsor.execute("select * from student")

result = mycorsor.fetchall()

for i in result:
    print(i)