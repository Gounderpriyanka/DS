import pymysql
import random

random.seed(42)

mydb = pymysql.connect(host="localhost",user="root",password="azdcgbjml")

mycursor = mydb.cursor()

mydb = pymysql.connect(host="localhost",user="root",password="azdcgbjml",database="society_db")
mycursor = mydb.cursor()

