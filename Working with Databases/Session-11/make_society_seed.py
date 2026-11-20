import pymysql
import random
from datetime import date

random.seed(42)

mydb = pymysql.connect(host="localhost",user="root",password="azdcgbjml")

mycursor = mydb.cursor()

mydb = pymysql.connect(host="localhost",user="root",password="azdcgbjml",database="society_db")
mycursor = mydb.cursor()

flats = {}

tower_blocks = ["A","B","C","D"]
bhk_numbers = [1,2,3]

for i in range(1,51):
    flats[i] = {
        "tower" : random.choice(tower_blocks),
        "bhk" : random.choice(bhk_numbers)  
    }
# for i,j in flats.items():
#     mycursor.execute(
#         "insert into flats values(%s,%s,%s)",
#         ( i,
#          j["tower"],
#          j["bhk"]

#         )
        
#         )
# mydb.commit()


meter_readings = {}
print(flats)
dates = []
for i in range(1,51):
    for j in range(1,13):
        dates.append(f"2025-{j}-01")
flat_id = []
for i in range(1,13):
    for j in range(1,51):
        flat_id.append(j)

units_kwh = []
print(flats[1]["bhk"])
for i in range(1,13):
    for j in range(1,51):
        if flats[j]["bhk"] == 1:
            units_kwh.append(random.randint(40,250))
        elif flats[j]["bhk"] == 2:
            units_kwh.append(random.randint(150,400))
        else:
            units_kwh.append(random.randint(250,600))

for i in range(1,601):
    meter_readings[i] = {
        "flat_id" : flat_id[i-1],
        "reading_month" :dates[i-1],
        "units_kwh": units_kwh[i-1],
        "bill_inr": units_kwh[i-1]*7.5
    } 

for i,data in meter_readings.items():
    mycursor.execute("Insert into meter_readings values(%s,%s,%s,%s,%s)",
            (i,
             data["flat_id"],
             data["reading_month"],
             data["units_kwh"],
             data["bill_inr"]

    ))
mydb.commit()