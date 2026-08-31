#1.Given the daily order counts for a Swiggy delivery partner over 10 days: 
# [12, 15, 17, 14, 13, 16, 200, 18, 14, 15], plot a simple graph (hand-drawn or using any tool) 
# and describe whether the data is left skewed, right skewed, or symmetrical. Explain your reasoning
#  based on the shape.

'''import matplotlib.pyplot as plt


l1 = [12, 15, 17, 14, 13, 16, 200, 18, 14, 15]

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.plot(days, l1, marker='o')

plt.xlabel("Days")
plt.ylabel("Number of Orders")
plt.title("Swiggy Daily Orders")

plt.show()'''

'''The data is right-skewed (positively skewed).
The reason is that most daily orders are between 12 and 18,
but there is one very large value, 200, on day 7.
This extreme value stretches the graph toward the right,
creating a long right tail.'''


#2.Take the following list of Instagram influencer follower counts (in thousands):
#  [5, 7, 8, 8, 9, 10, 12, 15, 95]. Calculate the mean and median, then state which is
#  higher and what that tells you about the skewness of the data.If the mean is pulled away from
#  the median, the data is skewed in that direction.
'''import numpy as np
data = [5, 7, 8, 8, 9, 10, 12, 15, 95]

mean = np.mean(data)
median = np.median(data)

print("Mean:",mean) # 18.777
print("Median:",median) # 9.0

if mean>median:
    print("Mean is higher than median.")
    print("The data is right-skewed")
'''


# 3.Find a real-world example of right-skewed data from any app you use (like Zomato order amounts, Paytm wallet balances,
#  or YouTube video views). Briefly describe the dataset and explain why you think it is right skewed.
'''import numpy as np
youtube_views = [100, 150, 200, 250, 300, 500, 800, 1500, 10000]


mean = np.mean(youtube_views)
median = np.median(youtube_views)
print(mean) # 1533.33
print(median) # 300.0'''

'''Mean > Median
Therefore, the data is right-skewed (positively skewed).'''


# 4.Given this dataset of Flipkart product ratings: [3, 3, 4, 4, 4, 5, 5, 5, 5, 5], draw a rough graph and 
# state if the distribution is symmetrical, left skewed, or right skewed. Justify your answer in one line.

import numpy as np
import matplotlib.pyplot as plt

ratings = [3, 3, 4, 4, 4, 5, 5, 5, 5, 5]

values, counts = np.unique(ratings, return_counts=True)

plt.bar(values, counts)

plt.xlabel("Flipkart Product Rating")
plt.ylabel("Frequency")
plt.title("Flipkart Product Ratings")

plt.show()
