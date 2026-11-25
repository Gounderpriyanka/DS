# Tasks 1.Write 'cricket_window_stats.py' in a folder named 'cricket_window_stats' with a list of runs
#  scored in each of 20 overs by a fictional team (values 2 to 18) and a function 
# `best_fixed_window(runs, k)` returning the first over number and total of the k consecutive overs
#  with the most runs. Slide the window by adding the new over and subtracting the one that leaves.
#  Test k = 3, 5 and 20. Constraint: Do not recompute with `sum(runs[i:i+k])`.



# def best_fixed_window(runs, k):
runs = [8, 12, 5, 15, 9, 11, 7, 14, 6, 10,
        18, 4, 13, 8, 16, 5, 12, 9, 7, 14]

def best_fixed_window(runs,k):
    windows = sum(runs[:k])
    max_sum = windows

    for i in range(k,len(runs)):
        windows = windows + runs[i] - runs[i-k]
        max_sum = max(windows,max_sum)
        
    return max_sum


print("k = 3:", best_fixed_window(runs, 3))
print("k = 5:", best_fixed_window(runs, 5))
print("k = 20:", best_fixed_window(runs, 20))