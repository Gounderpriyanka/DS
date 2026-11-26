# Task 1.Write a program named 'plan_lookup.py' inside a folder named 'recharge_plan_lab'.
#  Store at least 12 fictional mobile recharge plan prices (₹19 to ₹999) in ascending order in a list,
#  ask the user for a price, and use a for loop to find it. Print the plan's position and
#  how many plans were checked, or 'No plan at this price'. Test with 239 and 500. 
# Hint: `input()` returns text; convert it with `int()` before comparing.

l1 = [19, 49, 99, 149, 199, 239, 299, 399, 499, 599, 799, 999]

price = int(input("Enter your plan:"))

for i in range(0,len(l1)):
    if price == l1[i]:
        print(f"The plan position: {i+1}")
        print(f"The plan was checked {i+1} times")
        break
else:
    print("No plan at this price")

# task 2.Extend 'plan_lookup.py' with a second function that uses the fact that the prices 
# are in ascending order: stop the loop as soon as a plan price is bigger than the price entered,
#  and print how many plans were checked. Test with prices 19, 239, 100 and 2000, and
#  compare the checked counts with the first function.

l1 = [19, 49, 99, 149, 199, 239, 299, 399, 499, 599, 799, 999]

