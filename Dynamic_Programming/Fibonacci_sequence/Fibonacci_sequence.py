from typing import List

# This function will hold the memo dictionary object, used 
# for storing the result of the Fib_number function 

def Memorization(f):
    memo = {}
    def save_memo_and_pass_param(number):
        if number not in memo:
            memo[number] = f(number)
        return memo[number]
    return save_memo_and_pass_param

# Use the Memorization function as the decorator 
# on top of the Fib_number function

@Memorization    
def Fib_number(number:int):
    if number == 0:
        return 0
    if number <= 2:
        return 1
    return Fib_number(number - 1) + Fib_number(number - 2)


# TESTING #

test_numbers = [0, 1, 5, 25, 50, 100, 300]

# It shouldn't take too long to perform these test

for num in test_numbers:
    print(Fib_number(num))


