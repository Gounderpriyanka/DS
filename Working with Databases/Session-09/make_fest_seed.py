import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="azdcgbjml")
mycursor = mydb.cursor()

mycursor.execute("create database if not exists fest_db")
mydb.commit()

mydb = pymysql.connect(host="localhost",user="root",password="azdcgbjml",database="fest_db")
mycursor = mydb.cursor()

mycursor.execute("create table if not exists students(student_id int primary key,student_name varchar(50),Branch varchar(50),year int,referred_by varchar(50))" )
mydb.commit()

mycursor.execute("create table if not exists Events(event_id int primary key,event_name varchar(50),Fee_inr int, Hall varchar(50))")
mydb.commit()

mycursor.execute("Create table if not exists Registrations(reg_id int primary key,student_id int,foreign key(student_id) references students(student_id),event_id int ,foreign key(event_id) references Events(event_id),Reg_date date)")
mydb.commit()