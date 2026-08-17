#1.Create a Python script called playlist_stats.py that takes a list of daily Spotify song
#  play counts (e.g., [120, 135, 150, 200, 120, 90, 200]) and calculates the mean (average) 
# number of plays.

'''import  pandas as pd

playlist_stats = [120, 135, 150, 200, 120, 90, 200]
result = pd.Series(playlist_stats)
print(result.mean())
'''
# 2.Given the following array of delivery times (in minutes) for Zomato orders: 
# [30, 25, 40, 35, 30, 45, 30], write code to find the median delivery time and print it.

'''import pandas as pd
l1 = [30, 25, 40, 35, 30, 45, 30]

Result = pd.Series(l1)
print(Result.median())'''

#3.Write a function most_common_rating(ratings) that takes a list of Flipkart product ratings 
# (e.g., [5, 4, 4, 3, 5, 4, 2, 4]) and returns the mode (most frequent rating)

'''import pandas as pd
def  most_common_rating(ratings):
     Result = pd.Series(ratings).mode()
     return Result

l1 = [5, 4, 4, 3, 5, 4, 2, 4]
print(most_common_rating(l1))'''

#4.Given three lists representing YouTube video views for three different channels, 
# compare the mean, median, and mode for each channel, and decide which channel's data is 
# most affected by outliers.Hint: Try using one list with a very 
# high value (e.g., [100, 120, 110, 105, 5000]) to see the effect on mean vs median.

import pandas as pd


Channel_A = [100, 120, 110, 105, 115]
Channel_B = [100, 120, 110, 105, 5000]
Channel_C = [100, 120, 120, 110, 100]

channels = [Channel_A, Channel_B, Channel_C]

for i, channel in enumerate(channels, 1):
    data = pd.Series(channel)

    print(f"Channel {i}:")
    print("Mean:", data.mean())
    print("Median:", data.median())
    print("Mode:", data.mode().tolist())
    print()
