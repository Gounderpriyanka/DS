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

# students = {}
# branches = ["BCA", "BBA", "BTech", "BSc"]
# year = [1,2,3,4]

# referred_students = random.sample(range(2,61),25)


# for i in range(1,61):

    
#     if i in referred_students:
#         reffered_by = random.randint(1,i-1)
#     else:
#         reffered_by = None


#     students[i] = {
#         "student_name" : f"student_{i}",
#         "branches" : random.choice(branches),
#         "year" : random.choice(year),
#         "reffered_by" : reffered_by 
        
#     }
   
# print(students[1])
# for i,data in students.items():
#     mycursor.execute(
#         "Insert into students values(%s,%s,%s,%s,%s)",
#         (i,
#         data["student_name"],
#         data["branches"],
#         data["year"],
#         data["reffered_by"]

#         )
        
#     )

# mydb.commit()



Events = {}

event_name = [
    "Coding Challenge", "Web Design", "Quiz Competition",
    "Robotics", "Photography", "Debate Competition",
    "Dance Competition", "Music Competition"
]

fee_inr = [250, 200, 150, 100, 50, 100, 250, 200]

hall = [
    "Seminar Hall", "Computer Lab", "Main Hall",
    "Innovation Lab", "Arts Hall", "Conference Hall",
    "Auditorium", "Open Stage"
]

for i in range(1, 9):
    Events[i] = {
        "Event_name": event_name[i-1],
        "Fee_inr": fee_inr[i-1],
        "Hall": hall[i-1]
    }

for i , data in Events.items():
    mycursor.execute(
        "Insert into events values(%s,%s,%s,%s)",
        (
            i,data["Event_name"],data["Fee_inr"],data["Hall"]
        )
    )

mydb.commit()

