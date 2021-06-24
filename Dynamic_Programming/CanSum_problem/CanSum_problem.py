# Function with memo object

def CanSum(target_sum:int, number_list,memo = None):
    # Initialize the memo object if it is None
    if memo == None:
        memo = {}
    # Return the value if it is inside the memo object
    if target_sum in memo:
            return memo[target_sum]
    # Two base cases
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    # Go through each number in the array and call the function recursively
    for number in number_list:
        remainder = target_sum - number
        memo[remainder] = CanSum(remainder,number_list,memo)
        if memo[remainder] == True:
            return True
    return False

# Slow recursive function, placed here for reference

def CanSum_slow(target_sum:int, number_list):
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for number in number_list:
        remainder = target_sum - number
        if(CanSum_slow(remainder,number_list) == True):
            return True
    return False

# Test

test_result = CanSum(4823,[5,3,4,7,6,2,1])
print(test_result)