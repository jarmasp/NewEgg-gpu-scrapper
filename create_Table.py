from email import header
import mysql.connector
import csv
import sys

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='852456jose',
    database='gpuDataBase'
)

mycursor = db.cursor()

#mycursor.execute('CREATE DATABASE gpuDataBase')

#mycursor.execute('CREATE TABLE gpuPrice (Manufacturer VARCHAR(20), Brand VARCHAR(20), Model VARCHAR(20), Price SMALLINT UNSIGNED, Shipping VARCHAR(40), Link VARCHAR (155))')

csv_data = csv.reader(open('Graphics card price.csv'))

header = next(csv_data)

for row in csv_data:
    #print(row)
    mycursor.execute('INSERT INTO gpuPrice (Manufacturer, Brand, Model, Price, Shipping, Link) VALUES (%s, %s, %s, %s, %s, %s)', row)

db.commit()
mycursor.close()