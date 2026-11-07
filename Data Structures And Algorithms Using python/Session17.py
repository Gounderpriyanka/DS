#Write 'fd_growth_recursion.py' in a folder named 'fd_growth_recursion' with a recursive function 
# `fd_value(principal, rate_percent, years)` that returns a fixed deposit's value with yearly 
# compounding: for 0 years it returns the principal, otherwise it multiplies the previous year's 
# value by (1 + rate/100). Test ₹10000 at 7% for 0, 1 and 5 years, rounded to 2 decimals.
#  Constraint: Do not use loops or 

'''def fd_value(principal,rate_percent,years):
    if years == 0:
        return principal
    else:
        return round(fd_value(principal,rate_percent,years - 1)*(1+rate_percent/100),2)
print(fd_value(10000,7,5))'''


#2.Add a `depth` parameter (default 0) to `fd_value` so that it prints an indented line when each
#  call starts and when it returns, showing the principal, years and returned value, 
# for a 3-year deposit. Hint: print `' ' * depth` before the text and pass `depth + 1` in the 
# recursive call.


'''def fd_value(principal,rate_percent,years,depth = 0):
    print(" " * depth + f"Starting : {principal},years = {years} ")
    if years == 0:
        return principal
    else:
        value = round(fd_value(principal,rate_percent,years - 1,depth + 1)*(1+rate_percent/100),2)
    print (" " * depth + f"Returning: {value},years: {years}")
    return value
print(fd_value(10000,7,5))'''

#3.Add `fd_value_loop(principal, rate_percent, years)` that gives the same answer with a for loop.
#  Check that both versions give the same value for 5 years, then time both for 800 years with 
# `time.perf_counter()` and print both results and both times

def fd_value(principal,rate_percent,years):
    for i in range(0,years):
        value += round((principal,rate_percent,years)*(1+rate_percent/100),2)
    return value

fd_value(10000,7,5)



