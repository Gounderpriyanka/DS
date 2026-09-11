# 1.Write a Python function bayes_posterior(prior, likelihood, evidence) that calculates and
# returns the posterior probability using Bayes theorem formula for given values.

def bayes_posterior(prior, likelihood, evidence):
    posterior = (likelihood * prior) / evidence
    return posterior


# Example
prior = 0.10
likelihood = 0.80
evidence = 0.26

result = bayes_posterior(prior, likelihood, evidence)

print("Posterior Probability:", result)

# 2.Given the following scenario: On Swiggy, 10% of restaurants are 'premium', and 80% of premium
# restaurants offer a discount, while only 20% of regular restaurants do. If you see a discount,
# use Bayes theorem in code to find the probability that the restaurant is premium.
# Define prior, likelihood, and evidence in your code with comments.

def bayes_posterior(prior, likelihood, evidence):
    return (likelihood * prior) / evidence


# Prior probability of premium restaurant
prior = 0.10

# Probability of discount given premium restaurant
likelihood = 0.80

# Probability of discount
# = (0.80 * 0.10) + (0.20 * 0.90)
evidence = (0.80 * 0.10) + (0.20 * 0.90)

posterior = bayes_posterior(prior, likelihood, evidence)

print("Probability that the restaurant is premium:", posterior)

# 3.Simulate a basic spam detection filter: Given a list of 20 email subjects (some spam, some not),
# and the probability that 'free' appears in spam vs
#  non-spam emails, write code to calculate the 
# probability an email is spam if it contains 'free', using Bayes theorem.

def bayes_posterior(prior, likelihood, evidence):
    return (likelihood * prior) / evidence


# 20 email subjects
emails = [
    "Win free money now",
    "Meeting tomorrow",
    "Get free gift",
    "Project update",
    "Free lottery ticket",
    "Your order confirmation",
    "You won a free prize",
    "Team meeting",
    "Claim your free reward",
    "Interview schedule",
    "Free cash offer",
    "Monthly report",
    "Congratulations free voucher",
    "Assignment submission",
    "Free discount coupon",
    "Office meeting",
    "Earn free money",
    "Your bill is ready",
    "Free vacation offer",
    "Project discussion"
]

# Assume 8 emails are spam and 12 are non-spam
prior_spam = 8 / 20

# Probability of 'free' appearing in spam emails
likelihood = 0.75

# Probability of 'free' appearing in non-spam emails
prob_free_nonspam = 0.10

# Probability of seeing 'free'
evidence = (likelihood * prior_spam) + \
           (prob_free_nonspam * (1 - prior_spam))

posterior = bayes_posterior(prior_spam, likelihood, evidence)

print("Probability that the email is spam:", posterior)

# 4.Use ChatGPT or Copilot to generate a real-world Bayes theorem example related to any app you use
# (Instagram, Zomato, Flipkart, etc.), then write code to solve it and submit both the prompt you
# used and your code.

'''Give me a simple real-world Bayes theorem example related to Flipkart.
Include realistic probabilities and explain how to calculate the probability 
that a customer will buy a product after seeing a discount.'''


def bayes_posterior(prior, likelihood, evidence):
    return (likelihood * prior) / evidence


# Prior probability that customer will buy
prior = 0.30

# Probability of using discount if customer will buy
likelihood = 0.70

# Probability of using discount
evidence = (0.70 * 0.30) + (0.20 * 0.70)

posterior = bayes_posterior(prior, likelihood, evidence)

print("Probability that the customer will buy:", posterior)