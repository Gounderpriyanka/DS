# 1.Write down the null hypothesis (H0) and alternative hypothesis (H1) for the following scenario: 
# You believe that people spend more time on Instagram than on YouTube daily.

'''1. Null Hypothesis and Alternative Hypothesis

Null Hypothesis (H₀): People do not spend more time on Instagram than on YouTube daily.
Alternative Hypothesis (H₁): People spend more time on Instagram than on YouTube daily.'''

# 2.Given the data: Group A (users shown a new Zomato home page) had an average order value of 
# ₹350 from 30 users, and Group B (old home page) had an average order value of ₹320 from 30 users.
# Assume both groups have a standard deviation of ₹50. Calculate the p-value using a two-sample t-test
# (you may use Python, R, or an online calculator), and decide whether to accept or reject the null hypothesis
# at a 0.05 significance level.Use scipy.stats.ttest_ind in Python or 
# any online t-test calculator if you are not comfortable with code.

from scipy.stats import ttest_ind
import numpy as np

# Given data
mean_A = 350
mean_B = 320
std_A = 50
std_B = 50
n_A = 30
n_B = 30

# Calculate t-statistic manually
t = (mean_A - mean_B) / np.sqrt((std_A**2 / n_A) + (std_B**2 / n_B))

# Degrees of freedom
df = n_A + n_B - 2

# Calculate two-tailed p-value
from scipy.stats import t
p_value = 2 * t.sf(abs(t), df)

print("t-statistic:", t)
print("p-value:", p_value)



# 3.Pick any feature from your favorite app (like the new dark mode in WhatsApp or a redesigned payment
#  button in Paytm) and describe how you would set up an A/B test for it. Clearly state what your
#  control and variant groups would be, what metric you would measure, and what your null and 
# alternative hypotheses are.

'''
Feature: Redesigned payment button in Paytm.

Control Group: 50% of users see the old payment button.
Variant Group: 50% of users see the redesigned payment button.
Metric: Percentage of users who successfully complete a payment.

H₀: The new payment button does not improve the payment completion rate.

H₁: The new payment button improves the payment completion rate.

After collecting enough data, we compare the two groups using an appropriate statistical test 
and p-value.
'''

# 4.Suppose you run an A/B test for a new 'Add to Wishlist' button design on Flipkart. Out of 1000 users, 
# 520 clicked the new button versus 480 who clicked the old button. Without doing detailed calculations, 
# explain if this difference is likely to be significant or just due to chance. Briefly explain how the p-value
# helps you decide.

'''
Out of 1000 users:

New button: 520 clicks
Old button: 480 clicks

The difference is 40 clicks, or 52% vs 48%.

This difference may be due to chance, so we cannot conclude that the new button is better
 just by looking at the percentages.

The p-value helps us decide:

If p-value < 0.05 → reject H₀ → difference is statistically significant.
If p-value ≥ 0.05 → do not reject H₀ → difference may be due to chance.

So, we need a statistical test to calculate the p-value before deciding whether the
 new button is truly better.
'''