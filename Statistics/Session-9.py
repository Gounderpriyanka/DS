# 1.Generate 100 random numbers in Python that follow a normal distribution with
# mean 50 and standard deviation 10 using numpy, then plot the bell curve using matplotlib.

import numpy as np
import matplotlib.pyplot as plt

# Generate 100 random numbers
data = np.random.normal(loc=50, scale=10, size=100)

# Plot histogram
plt.hist(data, bins=10, density=True)

plt.title("Normal Distribution")
plt.xlabel("Values")
plt.ylabel("Density")
plt.show()

# 2.Given an array of 20 daily step counts from your fitness tracker app, 
# calculate the mean, median, and mode, and check if they are approximately equal
# as expected in a normal distribution.Use numpy.mean(), numpy.median(), and scipy.stats.mode().

import numpy as np
from scipy import stats

# Daily step counts for 20 days
steps = np.array([
    5000, 6000, 5500, 7000, 6500,
    6000, 5800, 6200, 5900, 6100,
    6000, 5700, 6300, 6400, 5600,
    6000, 5900, 6100, 6200, 5800
])

# Calculate mean, median and mode
mean = np.mean(steps)
median = np.median(steps)
mode = stats.mode(steps, keepdims=True).mode[0]

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

# Check if they are approximately equal
if abs(mean - median) < 500 and abs(median - mode) < 500:
    print("Mean, median and mode are approximately equal.")
else:
    print("They are not approximately equal.")


# 3.Simulate the scores of 200 players in an online game (e.g., PUBG, Free Fire) 
# using a normal distribution with mean 70 and standard deviation 15, then count
# how many players scored within one standard deviation (between 55 and 85) of the mean.
# Use the 68-95-99 rule to check your answer.

import numpy as np

# Generate scores of 200 players
scores = np.random.normal(loc=70, scale=15, size=200)

# Count players between 55 and 85
count = np.sum((scores >= 55) & (scores <= 85))

print("Number of players within one standard deviation:", count)
print("Percentage:", (count / 200) * 100)

# 4.Pick any real-world scenario (like delivery times for Zomato orders or playlist song 
# durations on Spotify) and explain in 3-4 lines why the normal distribution might be a 
# good fit for modeling this data.

"""
Zomato delivery times can sometimes be modeled using a normal distribution when considering
 many orders from a similar area and time period. Most orders may arrive around the average 
 delivery time, while fewer orders take much shorter or longer than average.
Factors like traffic and restaurant preparation can cause variation around the average. 
Therefore, a normal distribution can be a useful approximate model for delivery times.
"""