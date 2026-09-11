# 1.Create two Python lists: one representing the number of hours you spend on Instagram each day for a
# week, and another for the number of posts you make each day. Plot these as a scatter plot using matplotlib
# and visually describe whether the relationship looks like a positive, negative, or zero correlation.

import matplotlib.pyplot as plt

# Instagram usage hours for 7 days
hours = [1, 2, 3, 4, 5, 4, 6]

# Number of posts made each day
posts = [1, 2, 3, 4, 5, 4, 6]

# Scatter plot
plt.scatter(hours, posts)

plt.xlabel("Instagram Hours")
plt.ylabel("Number of Posts")
plt.title("Instagram Usage vs Posts")
plt.show()

# 2.Given the following data for 6 friends: their monthly Zomato order count and their monthly Swiggy order count,
#  calculate the correlation coefficient between the two lists using numpy's corrcoef(). 
# Print the result and explain if the correlation is positive, negative, or zero.


import numpy as np

# Monthly orders of 6 friends
zomato = [10, 15, 8, 20, 12, 18]
swiggy = [8, 14, 10, 18, 13, 16]

# Calculate correlation coefficient
correlation = np.corrcoef(zomato, swiggy)[0, 1]

print("Correlation coefficient:", correlation)

if correlation > 0:
    print("There is a positive correlation.")
elif correlation < 0:
    print("There is a negative correlation.")
else:
    print("There is zero correlation.")


# 3.Think of two variables from your daily life (for example, number of YouTube videos watched per day and
#  daily study hours). Write a short paragraph describing whether you expect a positive, negative, or
# zero correlation between them, and why.

'''
I expect the number of YouTube videos watched per day and daily study hours to have a 
negative correlation. If a person spends more time watching YouTube, they may have less
 time available for studying. Similarly, watching fewer videos may leave more time for study.
 However, this is only a possible relationship and does not mean one variable always causes the other.

'''
# 4.Use ChatGPT to generate a small dataset (10 pairs of numbers) that shows a strong negative correlation
# between time spent on Spotify and marks scored in a test. Paste the dataset and plot it as a scatter 
# plot using matplotlib.Ask ChatGPT to "generate 10 pairs of numbers with a strong negative correlation" and
# specify your variables.

'''
"Generate 10 pairs of numbers with a strong negative correlation between time spent on
 Spotify (hours per day) and marks scored in a test."
'''

import matplotlib.pyplot as plt

# Spotify hours and test marks
spotify_hours = [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
marks = [95, 91, 88, 84, 81, 76, 72, 68, 63, 58]

# Create scatter plot
plt.scatter(spotify_hours, marks)

plt.xlabel("Time Spent on Spotify (Hours)")
plt.ylabel("Test Marks")
plt.title("Spotify Time vs Test Marks")

plt.show()