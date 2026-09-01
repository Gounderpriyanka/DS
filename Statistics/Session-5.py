# 1.List 3 examples of 'population' and 'sample' in the context of apps you use daily
# (like Instagram followers, Zomato restaurants, or Flipkart products). For each, clearly define what 
# would be considered the population and what would be a sample.

'''Example 1: Instagram
Population: All followers of an Instagram account.
Sample: 100 randomly selected followers from those followers.

Example 2: Zomato
Population: All restaurants listed on Zomato.
Sample: 50 randomly selected restaurants.

Example 3: Flipkart
Population: All products available on Flipkart.
Sample: 200 randomly selected products.'''


# 2.Write a Python script that simulates random sampling: given a list of 1000 fake user IDs
# (e.g., user1 to user1000), select 50 random users to simulate a survey sample.
# Print the selected user IDs.Use the random.sample() function from Python's random module.

import random
user = [f"user{i}" for i in range(1,1001)]
sample_users = random.sample(user,50)
print("Selected 50's student")
for i in sample_users:
    print(i)

# 3.Imagine you are analyzing food delivery times on Swiggy. Explain in 2-3 sentences why you would use sampling 
# instead of collecting data from every single order ever made.

'''We use sampling because Swiggy may have millions of orders, and collecting data from every order 
would require a lot of time and resources. A properly selected sample can provide useful information
about overall delivery times more quickly and efficiently.'''

# 4.Given this scenario: A survey about music preferences is only sent to users who recently streamed Bollywood 
# songs on Spotify. Identify and explain the type of bias this introduces in the sample.

'''This introduces selection bias or sampling bias. 
Since the survey is sent only to users who recently streamed Bollywood songs,
users who listen to other types of music are excluded.
Therefore, the sample may not represent all Spotify users accurately.'''

# 5.Choose any two types of sampling (for example: random sampling, stratified sampling, systematic sampling, 
# cluster sampling). For each, describe how you would use it to select a sample of users from BookMyShow to
# study movie booking habits.

'''1. Random Sampling

We can take the list of all BookMyShow users and randomly select 500 users.
Every user has an equal chance of being selected.

Population: All BookMyShow users
Sample: 500 randomly selected users

2. Stratified Sampling

We can divide BookMyShow users into different age groups, such as 18-25, 26-35, 36-50, 
and 51+. Then, randomly select users from each group.

Example:

18 - 25  → 100 users
26 - 35  → 100 users
36 - 50  → 100 users
51 +    → 100 users

Total Sample = 400 users'''