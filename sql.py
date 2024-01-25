import sqlite3

## connect to sqlite
connection=sqlite3.connect("student.db")

## create a cursor object to insert record , create table , retrieve 
cursor=connection.cursor()
# create the table 
table_info= """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SELECTION VARCHAR(25),MARKS INT);
"""
cursor.execute(table_info)

## insert some more records 

cursor.execute('''Insert Into STUDENT values('Chirag','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Vijay','Data Science','A',100)''')
cursor.execute('''Insert Into STUDENT values('Parth','Data Science','B',82)''')
cursor.execute('''Insert Into STUDENT values('Dev','Devops','A',100)''')
cursor.execute('''Insert Into STUDENT values('Atharva','Devops','A',90)''')

## Display all the records 
print("The inserted records are") 
data=cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

## close the table
connection.commit()
connection.close()