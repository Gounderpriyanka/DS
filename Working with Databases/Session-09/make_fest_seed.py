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

referred_students = random.sample(range(2,61),25)
for i in range(1,61):
    if i in referred_students:
        reffered_by = random.randint(1,i-1)
    else:
        reffered_by = None



for i in range(1,61):
    students[i] = {
        "student_name" : f"student_{i}",
        "branches" : random.choice(branches),
        "year" : random.choice(year),
        "reffered_by" : reffered_by 
        
    }
   
print(students[1])

mycursor.execute(f"Insert into students values({students.items()})")
