#1.Given the daily order counts for a Swiggy delivery partner over 10 days: 
# [12, 15, 17, 14, 13, 16, 200, 18, 14, 15], plot a simple graph (hand-drawn or using any tool) 
# and describe whether the data is left skewed, right skewed, or symmetrical. Explain your reasoning
#  based on the shape.


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

l1 = [12, 15, 17, 14, 13, 16, 200, 18, 14, 15]

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.plot(days, l1, marker='o')

plt.xlabel("Days")
plt.ylabel("Number of Orders")
plt.title("Swiggy Daily Orders")

plt.show()