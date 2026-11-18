# Tasks 1.Write 'cricket_window_stats.py' in a folder named 'cricket_window_stats' with a list of runs
#  scored in each of 20 overs by a fictional team (values 2 to 18) and a function 
# `best_fixed_window(runs, k)` returning the first over number and total of the k consecutive overs
#  with the most runs. Slide the window by adding the new over and subtracting the one that leaves.
#  Test k = 3, 5 and 20. Constraint: Do not recompute with `sum(runs[i:i+k])`.

l1 = [8, 12, 5, 15, 9, 11, 7, 14, 6, 10, 18, 4, 13, 8, 16, 5, 12, 9, 7, 14]

k = 3
k = 5
k = 20

# def best_fixed_window(runs, k):
window_sum = sum(l1[:3]) #25
best_sum = window_sum 
best_index = 0


print(window_sum)


runs = [8, 12, 5, 15, 9, 11, 7, 14, 6, 10,
        18, 4, 13, 8, 16, 5, 12, 9, 7, 14]


def best_fixed_window(runs, k):

    window_sum = sum(runs[:k])
    best_sum = window_sum
    best_index = 0

    for i in range(k, len(runs)):

        window_sum = window_sum - runs[i - k] + runs[i]

        if window_sum > best_sum:
            best_sum = window_sum
            best_index = i - k + 1

    return best_index + 1, best_sum


print("k = 3:", best_fixed_window(runs, 3))
print("k = 5:", best_fixed_window(runs, 5))
print("k = 20:", best_fixed_window(runs, 20))