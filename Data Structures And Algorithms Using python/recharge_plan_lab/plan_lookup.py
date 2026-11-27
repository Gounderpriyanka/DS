# Task 1.Write a program named 'plan_lookup.py' inside a folder named 'recharge_plan_lab'.
#  Store at least 12 fictional mobile recharge plan prices (₹19 to ₹999) in ascending order in a list,
#  ask the user for a price, and use a for loop to find it. Print the plan's position and
#  how many plans were checked, or 'No plan at this price'. Test with 239 and 500. 
# Hint: `input()` returns text; convert it with `int()` before comparing.

'''l1 = [19, 49, 99, 149, 199, 239, 299, 399, 499, 599, 799, 999]

price = int(input("Enter your plan:"))

for i in range(0,len(l1)):
    if price == l1[i]:
        print(f"The plan position: {i+1}")
        print(f"The plan was checked {i} times")
        break
else:
    print("No plan at this price")
'''
# task 2.Extend 'plan_lookup.py' with a second function that uses the fact that the prices 
# are in ascending order: stop the loop as soon as a plan price is bigger than the price entered,
#  and print how many plans were checked. Test with prices 19, 239, 100 and 2000, and
#  compare the checked counts with the first function.

'''l1 = [19, 49, 99, 149, 199, 239, 299, 399, 499, 599, 799, 999]

def price(l1):
    price = int(input("Enter a value:"))
    for i in range(len(l1)):
        if  l1[i]>price:
            print("The Plan was checked",i)
            break
        elif price == l1[i]:
            print("The Plan was checked",i)
            print("Found")
            break
    else:
        print("The Plan was checked",i+1)
        print("Not found")
        
price(l1)
'''

# task 3.Add a dictionary named `plan_validity` to 'plan_lookup.py' that maps each plan price to its
#  validity in days (28, 56 or 84), and a third function that finds the validity of a price with
#  one dictionary lookup. Print 'No plan at this price' for a missing price.
#  Constraint: Do not use any loop inside this function.


plan_validity = {
    19: 28,
    49: 28,
    99: 28,
    149: 56,
    199: 56,
    239: 56,
    299: 56,
    399: 84,
    499: 84,
    599: 84,
    799: 84,
    999: 84
}


def validity(plan_validity):
    price = int(input("Enter the price: "))
    result = plan_validity.get(price,"Not found!")
    print(result)
validity(plan_validity)

# task 4.Finish 'plan_lookup.py' with a menu where the user picks method 1 (full scan),
#  2 (early stop) or 3 (dictionary), enters a price, and sees the number of steps that method used. 
# Run prices 19, 239, 100 and 2000 on all three methods and paste the outputs as comments at the end. 
# Create a GitHub repository named 'dsa_python_portfolio' and push the folder 'recharge_plan_lab' to it.

l1 = [19, 49, 99, 149, 199, 239, 299, 399, 499, 599, 799, 999]

plan_validity = {
    19: 28,
    49: 28,
    99: 28,
    149: 56,
    199: 56,
    239: 56,
    299: 56,
    399: 84,
    499: 84,
    599: 84,
    799: 84,
    999: 84
}

def full_scan(l1,price):
    
    for i in range(0,len(l1)):
        if price == l1[i]:
            print(f"The plan position: {i+1}")
            print(f"The plan was checked {i+1} times")
            break
    else:
        print("No plan at this price")
        print("The plan was checked", len(l1), "times")

def early_stop(l1,price):
    
    for i in range(len(l1)):
        if  l1[i]>price:
            print("The Plan was checked",i+1)
            break
        elif price == l1[i]:
            print("The Plan was checked",i+1)
            print("Found")
            break
    else:
        print("The Plan was checked",len(l1))
        print("Not found")


def validity(plan_validity, price):

    result = plan_validity.get(price)

    if result:
        print("Plan validity:", result, "days")
    else:
        print("No plan at this price")

    print("The plan was checked 1 time")

print("----- Recharge Plan Lookup -----")
print("1. Full Scan")
print("2. Early Stop")
print("3. Dictionary Lookup")

method = int(input("Choose method (1/2/3): "))
price = int(input("Enter the price: "))

if method == 1:
    full_scan(l1,price)
elif method == 2:
    early_stop(l1,price)
elif method == 3:
    validity(plan_validity,price)
else:
    print("Invalid method!")