import pymysql
import random
from datetime import date,timedelta

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



# Events = {}

# event_name = [
#     "Coding Challenge", "Web Design", "Quiz Competition",
#     "Robotics", "Photography", "Debate Competition",
#     "Dance Competition", "Music Competition"
# ]

# fee_inr = [250, 200, 150, 100, 50, 100, 250, 200]

# hall = [
#     "Seminar Hall", "Computer Lab", "Main Hall",
#     "Innovation Lab", "Arts Hall", "Conference Hall",
#     "Auditorium", "Open Stage"
# ]

# for i in range(1, 9):
#     Events[i] = {
#         "Event_name": event_name[i-1],
#         "Fee_inr": fee_inr[i-1],
#         "Hall": hall[i-1]
#     }

# for i , data in Events.items():
#     mycursor.execute(
#         "Insert into events values(%s,%s,%s,%s)",
#         (
#             i,data["Event_name"],data["Fee_inr"],data["Hall"]
#         )
#     )

# mydb.commit()

Registrations = {}
all_pairs = []
for i in range(1,51):
    for j in range(1,7):
        all_pairs.append((i,j))

print(all_pairs) 

selected_pairs = random.sample(all_pairs,200)
student_id = []
event_id = []
for  i , j in selected_pairs:
    student_id.append(i)
    event_id.append(j)



start_date = date(2026,10,1)
end_date = date(2026,10,31)

dayss = (end_date-start_date).days



for  i in range(1,len(student_id)+1):
    # get student_id and event_id from pair
    # create reg_date
    # INSERT into registrations
    reg_date = start_date + timedelta(days=random.randint(0,dayss))
    Registrations[i]  = {
        "student_id" : student_id[i-1],
        "event_id": event_id[i-1],
        "reg_date" : reg_date
    }

print(Registrations)

for i ,j in Registrations.items():
    mycursor.execute(
        "Insert into registrations values(%s,%s,%s,%s)",
        (
          i,j["student_id"],j["event_id"],j["reg_date"]  
        )
    )

mydb.commit()




