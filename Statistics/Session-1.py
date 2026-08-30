# Task 1
# List 5 daily actions performed on apps and identify
# whether the data generated is Numerical or Categorical.

actions = [
    ("Instagram", "Number of likes", 150, "Numerical"),
    ("Instagram", "Type of post", "Reel", "Categorical"),
    ("Zomato", "Restaurant rating", 4.5, "Numerical"),
    ("Flipkart", "Product category", "Electronics", "Categorical"),
    ("Flipkart", "Product price", 1499, "Numerical")
]
for app, action, data, data_type in actions:
    print("App:", app)
    print("Action:", action)
    print("Data:", data)
    print("Data Type:", data_type)
    print()


# Task 2
# Classify the music app data.


print("\nReason:")
print("This is categorical data because the values represent")
print("different music genres rather than measurable quantities.")
print()


# Task 3
# Statistics applied to an Instagram feature.


print("\nStatistics can help analyze user engagement.")
print("Mean and median can show the typical number of likes")
print("and help understand which content users prefer.")
print()


# Task 4
# Three basic statistical terms useful for a playlist
# recommendation system.

print("1. Mean:")
print("If a user listens to 20, 30 and 40 songs per day,")
print("the mean number of songs is 30.")

print("\n2. Median:")
print("If listening times are 2, 3, 4, 5 and 10 minutes,")
print("the median listening time is 4 minutes.")

print("\n3. Mode:")
print("If a user listens to Pop 10 times, Rock 5 times,")
print("and Jazz 3 times, Pop is the mode.")


