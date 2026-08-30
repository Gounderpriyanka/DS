#1.Given the daily order counts for a Swiggy delivery partner over 10 days: 
# [12, 15, 17, 14, 13, 16, 200, 18, 14, 15], plot a simple graph (hand-drawn or using any tool) 
# and describe whether the data is left skewed, right skewed, or symmetrical. Explain your reasoning
#  based on the shape.


'''import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

l1 = [12, 15, 17, 14, 13, 16, 200, 18, 14, 15]

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.plot(days, l1, marker='o')

plt.xlabel("Days")
plt.ylabel("Number of Orders")
plt.title("Swiggy Daily Orders")

plt.show()'''

#2.Take the following list of Instagram influencer follower counts (in thousands):
#  [5, 7, 8, 8, 9, 10, 12, 15, 95]. Calculate the mean and median, then state which is
#  higher and what that tells you about the skewness of the data.If the mean is pulled away from
#  the median, the data is skewed in that direction.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = [5, 7, 8, 8, 9, 10, 12, 15, 95]

df = pd.DataFrame({
    "instagram_user" : range(1,10),
    "data" : [5, 7, 8, 8, 9, 10, 12, 15, 95]
})

print(df)