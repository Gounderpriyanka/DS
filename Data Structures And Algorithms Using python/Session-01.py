#1.Write a program named 'plan_lookup.py' inside a folder named 'recharge_plan_lab'.
#Store at least 12 fictional mobile recharge plan prices (₹19 to ₹999) in ascending order in a list,
#  ask the user for a price, and use a for loop to find it. Print the plan's position and 
# how many plans were checked, or 'No plan at this price'. Test with 239 and 500.
#  Hint: `input()` returns text; convert it with `int()` before comparing.

l1 = [19, 49, 99, 149, 199, 239, 299, 399, 499, 599, 799, 999]


price = int(input("Enter Plan Price:"))
count = 0
found = False
for i in range(0,len(l1)):
    count +=1
    if price == l1[i]:
        found = True
        print("Plan found at position",count)
        print("Plans checked: ",count)
        break
        


if found == False:
    print("No plan at this price")
    print("plan checked:",count)


#2.Extend 'plan_lookup.py' with a second function that uses the fact that the prices are in
#  ascending order: stop the loop as soon as a plan price is bigger than the price entered,
#  and print how many plans were checked. Test with prices 19, 239, 100 and 2000, and
#  compare the checked counts with the first function.

l1 = [19, 49, 99, 149, 199, 239, 299, 399, 499, 599, 799, 999]


price = int(input("Enter Plan Price:"))
count = 0
found = False
for i in range(0,len(l1)):
    count +=1
    if price == l1[i]:
        found = True
        print("Plan found at position",count)
        print("Plans checked: ",count)
        break
    elif price >l1[i]:
        print("No plan at this price")
        break
        


if found == False:
    print("No plan at this price")
    print("plan checked:",count)

#3.Add a dictionary named `plan_validity` to 'plan_lookup.py' that maps each plan price to its
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

price = int(input("Enter the Plan Price:"))

if price in plan_validity:
    print("Validity:",plan_validity[price])
else:
    
