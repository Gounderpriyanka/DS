# 1.Write a Python function calculate_probability(event_count, total_outcomes)
# that returns the probability of an event, and use it to find the probability 
# of getting 'Heads' when tossing a coin.

def calculate_probability(event_count, total_outcomes):
    return event_count / total_outcomes


# For a fair coin:
# 1 outcome is Heads out of 2 possible outcomes
probability = calculate_probability(1, 2)

print("Probability of getting Heads:", probability)


# 2.Simulate rolling a six-sided dice 100 times using Python's random module,
# count how many times a '6' appears, and calculate the experimental probability
# of getting a '6'.Use random.randint(1,6) in a loop and keep a counter for '6'.

import random

six_count = 0

# Roll the dice 100 times
for i in range(100):
    roll = random.randint(1, 6)

    if roll == 6:
        six_count += 1

# Experimental probability
probability = six_count / 100

print("Number of times 6 appeared:", six_count)
print("Experimental probability:", probability)

# 3.Given an array of genres from your last 20 Spotify songs 
# (like ['pop', 'rock', 'pop', 'hiphop', ...]), write code to calculate the probability
# of randomly picking a 'pop' song from your recent history.

genres = [
    'pop', 'rock', 'pop', 'hiphop', 'pop',
    'jazz', 'rock', 'pop', 'hiphop', 'pop',
    'rock', 'pop', 'jazz', 'pop', 'rock',
    'hiphop', 'pop', 'rock', 'pop', 'jazz'
]

pop_count = genres.count('pop')
total_songs = len(genres)

probability = pop_count / total_songs

print("Number of Pop songs:", pop_count)
print("Total songs:", total_songs)
print("Probability of picking a Pop song:", probability)

# 4.Write a function that, given two arrays — one for users who ordered food on Zomato and 
# one for users who ordered dessert — calculates the probability that a randomly selected 
# user ordered both food and dessert (i.e., intersection over total unique users).

def probability_both(food_users, dessert_users):
    # Convert lists to sets
    food = set(food_users)
    dessert = set(dessert_users)

    # Users who ordered both
    both = food.intersection(dessert)

    # All unique users
    total_users = food.union(dessert)

    return len(both) / len(total_users)


food_users = [1, 2, 3, 4, 5, 6]
dessert_users = [3, 4, 6, 7, 8]

probability = probability_both(food_users, dessert_users)

print("Probability of ordering both:", probability)

# 5.Explain with a short Python code example how conditional probability could be used to
# improve recommendations in an app like Flipkart (e.g., probability of buying headphones
#  given user bought a phone).Use counts of users who bought both items vs total who bought a phone.

def conditional_probability(both_users, phone_users):
    return both_users / phone_users


# 100 users bought a phone
phone_users = 100

# 30 of them also bought headphones
both_users = 30

probability = conditional_probability(both_users, phone_users)

print("Probability of buying headphones given phone purchase:",
      probability)
