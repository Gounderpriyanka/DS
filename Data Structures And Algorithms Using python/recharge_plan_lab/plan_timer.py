# task 1 Write a program named 'plan_timer.py' in your 'recharge_plan_lab' folder with a function 
# `total_price(prices)` that adds up a list of prices using one for loop. 
# Build lists of 1000, 2000 and 4000 random prices with `random.randint(19, 999)`,
#  time each call with `time.perf_counter()`, and print a table of n and seconds taken. 
# Constraint: Do not use the built-in `sum()`.

import random
import time

def total_price(prices):
    total = 0
    for i in prices:
        total += i
    return total

print(" n         seconds")
for n in [1000,2000,4000]:
    price = []
    for i in range(n):
        price.append(random.randint(19,999))

    start = time.perf_counter()

    total_price(price)

    end = time.perf_counter()

    elapsed = end - start

    print(n,"     ",elapsed)

# task 2.Add a function `count_pairs(prices, target)` to 'plan_timer.py' that uses two nested loops
#  to count pairs of different plans whose prices add up to exactly 1000.
#  Time it on the same three list sizes and print a table that also shows, beside each time,
#  how many times bigger it is than the previous row's time.


def count_pairs(prices, target):
    count = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] + prices[j] == target:
                count += 1

    return count


print("\nTask 2")
print(" n         seconds        times bigger")

previous_time = None

for n in [1000, 2000, 4000]:

    price = []

    for i in range(n):
        price.append(random.randint(19, 999))

    start = time.perf_counter()

    pairs = count_pairs(price, 1000)

    end = time.perf_counter()

    elapsed = end - start

    if previous_time is None:
        print(n, "     ", elapsed, "        -")
    else:
        print(n, "     ", elapsed, "        ", elapsed / previous_time)

    previous_time = elapsed

 #Task 3.Add a function `first_above(prices, limit)` that returns the position of the first price 
 # above the limit, or -1. On a list of 200000 random prices, time it for the best case 
 # (limit 0, so the first item matches) and the worst case (limit 5000, so nothing matches),
 #  and print both times with 6 decimal places. Hint: the f-string format `{value:.6f}` prints 6 decimals.

