import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='852456jose',
    database='gpuDataBase'
)

mycursor = db.cursor()

mycursor.execute()