# Task-1
#Write a Python program that takes a list of cricket scores and a target score as input,
#then searches if the target score exists in the list and prints its index if found, 
# or 'Not Found' if not.

l1 = [12, 45, 78, 30, 56]
target_score = int(input("Enter the Target Score:"))

for i in range(0,len(l1)):
    if l1[i] == target_score:
        print(i)
        break
else:
    print("Not Found!")


# Task 2
#Write a Java program that takes a list of cricket scores and searches for a specific 
# score entered by the user, printing 'Found' or 'Not Found'.

l2 = [12, 45, 78, 30, 56]
search_score = int(input("Enter the Search Score: "))
for i in l2:
    if  i==search_score:
        print("Found")
        break
else:
    print("Not found")

#Task 3
# Imagine you are building a Zomato-style app: create a Python list of restaurant names,
#  then write a function search_restaurant(name) that returns True if the restaurant exists 
# in the list, otherwise False.

restaurant_name = ["Spice Garden", "Pizza Corner", "Green Bowl", "Tandoori House"]
def search_restaurant:
