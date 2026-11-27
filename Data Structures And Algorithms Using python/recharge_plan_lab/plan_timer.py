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

price = []
for i in range(1000):
    price.append(random.randint(19,999))

start = time.perf_counter()

total_price(price)

end = time.perf_counter()

elapsed = end - start

print(elapsed)

