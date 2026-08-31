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

import pandas as pd
data = [5, 7, 8, 8, 9, 10, 12, 15, 95]

df = pd.DataFrame({
    "instagram_user" : range(1,10),
    "data" : [5, 7, 8, 8, 9, 10, 12, 15, 95]
})
print(df)
mean = df["data"].mean()
median = df["data"].median()

print("Mean:",mean)
print("Median:",median)

if mean>median:
    print("Mean is higher than median.")
    print("The data is right-skewed")




# 3.Find a real-world example of right-skewed data from any app you use (like Zomato order amounts, Paytm wallet balances,
#  or YouTube video views). Briefly describe the dataset and explain why you think it is right skewed.



# 4.Given this dataset of Flipkart product ratings: [3, 3, 4, 4, 4, 5, 5, 5, 5, 5], draw a rough graph and 
# state if the distribution is symmetrical, left skewed, or right skewed. Justify your answer in one line.
