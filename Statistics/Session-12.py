# 1.Given two 2x2 matrices representing the number of likes and comments on two Instagram posts over two days,
# write Python code to multiply them and display the resulting matrix.


import numpy as np

post_data_day1 = np.array([[120, 15],
                           [200, 25]])

post_data_day2 = np.array([[2, 1],
                           [1, 3]])

result = np.matmul(post_data_day1, post_data_day2)

print("Resulting matrix:")
print(result)

# 2.Create a simple Python function linear_regression_predict(x, m, c) that takes an input value x,
# slope m, and intercept c, and returns the predicted output y for a linear regression equation y = mx + c.

def linear_regression_predict(x, m, c):
    y = m * x + c
    return y

print(linear_regression_predict(5, 4, 10))

# 3.Imagine you are predicting the delivery time for Zomato orders based on distance. Given three distances
#  (2km, 5km, 8km) and a linear regression equation y = 4x + 10 (where y is minutes), use your function
# from the previous task to calculate the predicted delivery time for each distance.

def linear_regression_predict(x, m, c):
    return m * x + c

distances = [2, 5, 8]

for x in distances:
    time = linear_regression_predict(x, 4, 10)
    print("Distance:", x, "km, Delivery Time:", time, "minutes")

# 4.Explain in your own words what the slope and intercept represent in the context of Flipkart's product
# price prediction (e.g., predicting price based on product rating). Write 2-3 sentences for each term.

""" 
Slope:
The slope shows how much the product price is expected to change when the product 
rating increases by 1 point. For example, a positive slope means products with higher
 ratings are predicted to have higher prices.

Intercept:
The intercept is the predicted product price when the rating is 0.
 It represents the starting value of the prediction before considering the effect of the rating.

"""

# 5.Use ChatGPT to ask: 'How does matrix multiplication help in training a machine learning model like Spotify's
# song recommendation system?' Summarize the answer in your own words in 3-4 sentences.

"""
Matrix multiplication helps Spotify connect users and songs based on their listening preferences.
One matrix can represent users and another can represent songs, while their values represent 
preferences or features. Multiplying these matrices helps calculate how strongly a user may
like a particular song. Spotify can then use these predicted preferences to recommend songs
the user is likely to enjoy.

"""