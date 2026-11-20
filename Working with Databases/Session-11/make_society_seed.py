import pymysql
import random

random.seed(42)

mydb = pymysql.connect(host="localhost",user="root",password="azdcgbjml")

mycursor = mydb.cursor()

mydb = pymysql.connect(host="localhost",user="root",password="azdcgbjml",database="society_db")
mycursor = mydb.cursor()

# flats = {}

# tower_blocks = ["A","B","C","D"]
# bhk_numbers = [1,2,3]

# for i in range(1,51):
#     flats[i] = {
#         "tower" : random.choice(tower_blocks),
#         "bhk" : random.choice(bhk_numbers)  
#     }
# for i,j in flats.items():
#     mycursor.execute(
#         "insert into flats values(%s,%s,%s)",
#         ( i,
#          j["tower"],
#          j["bhk"]

#         )
        
#         )
# mydb.commit()


