import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="azdcgbjml")
mycursor = mydb.cursor()

mycursor.execute("create database if not exists auto_db")
mydb.commit

mydb = pymysql.connect(host="localhost",user="root",password="azdcgbjml",database="auto_db")
mycursor = mydb.cursor()

mycursor.execute("create table drivers (driver_id int primary key auto_increment,driver_name varchar(50),)")