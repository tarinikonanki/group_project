# U: Check if number is even
# C: I will use mod
def is_even(n): #A- I will be using mod division to get the remainder and if it equals 0 it will be true, if else it will be false
    if n % 2 == 0:
        return True
    else: #S
        return False
# E- evaluate
print(is_even(4))
print(is_even(5))