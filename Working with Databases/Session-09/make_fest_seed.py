import pymysql
import random

random.seed(42)


mydb = pymysql.connect(host="localhost",user="root",password="azdcgbjml")
mycursor = mydb.cursor()

mycursor.execute("create database if not exists fest_db")
mydb.commit()

mydb = pymysql.connect(host="localhost",user="root",password="azdcgbjml",database="fest_db")
mycursor = mydb.cursor()

mycursor.execute("create table if not exists students(student_id int primary key,student_name varchar(50),Branch varchar(50),year int,referred_by int)" )
mydb.commit()

mycursor.execute("create table if not exists Events(event_id int primary key,event_name varchar(50),Fee_inr int, Hall varchar(50))")
mydb.commit()

mycursor.execute("Create table if not exists Registrations(reg_id int primary key,student_id int,foreign key(student_id) references students(student_id),event_id int ,foreign key(event_id) references Events(event_id),Reg_date date)")
mydb.commit()

students = {}
branches = ["BCA", "BBA", "BTech", "BSc"]
year = [1,2,3,4]

reffered_id = []
for i in range(1,61):
    if random(25):
        reffered_id.append(random.randint(1,i-1))
    else :
        reffered_id.append(None)

for i in range(1,61):
    students[i] = {
        "student_name" : f"student_{i}",
        "branches" : random.choice(branches),
        "year" : random.choice(year),
        "referred_id" : reffered_id[i-1]
    }
   




print(students[1])



