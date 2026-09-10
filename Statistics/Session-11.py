# 1.Create a Python list to represent a playlist of 5 song durations in seconds
# (e.g., [210, 180, 245, 200, 175]). Print the total duration of the playlist.

'''l1 = [210,180,245,200,175]

total_duration = sum(l1)

print("Total duration:", total_duration, "seconds")'''


# 2.Represent a 3x3 matrix in Python to store the ratings (1-5) given by 3 friends to 3 different 
# food items on Swiggy. Print the matrix and display the rating each friend gave to the second food item.

'''ratings = [
    [5, 4, 3],
    [4, 5, 4],
    [3, 4, 5]
]

print("Ratings Matrix:")
print(ratings)

print("Rating given by each friend to the second food item:")

for row in ratings:
    print(row[1])'''

# 3.Given a matrix representing the number of orders for 4 different dishes across 3 days 
# (rows: days, columns: dishes), write code to calculate and print the total orders for each dish.

orders = [
    [10, 15, 20, 12],
    [12, 18, 15, 10],
    [8,  20, 17, 15]
]

dish_totals = [0, 0, 0, 0]

for row in orders:
    for i in range(4):
        dish_totals[i] += row[i]

print("Total orders for each dish:")
print(dish_totals)

# 4.Imagine you have a table of 5 Flipkart products with columns for price and quantity sold.
# Represent this data as a matrix in Python, then write a function to calculate the total revenue 
# for each product.Multiply price and quantity for each row, then print the results.

products = [
    [500, 10],
    [1200, 5],
    [800, 8],
    [1500, 4],
    [300, 15]
]

def calculate_revenue(price, quantity):
    return price * quantity

for product in products:
    price = product[0]
    quantity = product[1]
    revenue = calculate_revenue(price, quantity)
    print("Revenue:", revenue)