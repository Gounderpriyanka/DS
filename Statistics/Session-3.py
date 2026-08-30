# 1.Given an array of daily step counts from your fitness app for one week 
# (e.g., [4500, 7000, 5000, 8000, 4000, 9000, 6000]), calculate the variance by hand using the variance
# formula and show each calculation step.

'''import numpy as np
arr = np.array([4500, 7000, 5000, 8000, 4000, 9000, 6000])
print("Variance:",np.var(arr))'''

# 2.Write a Python function called calculate_standard_deviation(scores) that takes a list of exam scores 
# and returns the standard deviation rounded to two decimal places.

'''import numpy as np
l1 = [80, 75, 90, 85, 70]
def calculate_standard_deviation(scores):
    arr = np.array([scores])
    return np.std(arr)
print(calculate_standard_deviation(l1))'''

# 3.Imagine two friends track their daily spending on Zomato over 5 days. Friend A spends [200, 200, 200, 200, 200]
# and Friend B spends [100, 300, 150, 400, 50]. Calculate the standard deviation for both and
# explain in 2-3 lines who has more consistent spending and why.

'''import numpy as np
friend_A = [200, 200, 200, 200, 200]
friend_B = [100, 300, 150, 400, 50]

std_A = np.std(friend_A)
std_B = np.std(friend_B)

print("Friend A Standard Deviation =",std_A)
print("Friend B Standard Deviation =",std_B)
print("Friend A has more consistent spending because the standard deviation is 0 Friend B spending varies significantly from day to day, resulting in a higher standard deviation.")'''

# 4.You are given the monthly salary data of 6 employees in a startup:
# [28000, 29000, 27000, 60000, 26500, 27500]. Calculate the variance and standard deviation, then interpret 
# in 2-3 lines what the high or low spread means for this team.

import numpy as np
l1 = [28000, 29000, 27000, 60000, 26500, 27500]
print("Mean Salary : ",np.mean(l1))
print("Variance : ",np.var(l1))
print("Standard Deviation : ",np.std(l1))

print("The team has a high spread in salaries because one employee earns ₹60,000,
while most employees earn around ₹26,500–₹29,000. This high standard deviation
shows that salaries are not evenly distributed across the team.")