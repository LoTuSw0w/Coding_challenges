# QUESTION
Write a function called canSum(targetSum, numbers) that returns True only if the numbers in the array can sum to the target sum. All the numbers in the array are positive integers and you can use them more than once for the solution.

Example:
```
# True case
Input: number = 7, number_list = [2,3,4]
Output: True
# False case
Input: number = 10, number_list = [7,2]
Output: False
```

# How I solve it:

Instead of finding the sum of each number, I would take the target number then subtract it by each number in the list. However, when using normal recursion, the function would take an astronomically huge runtime of O(m^n) (m is the array length, n is the target sum), since now each "target_sum" in the recursion tree would have to go through all the numbers in the array:

```python
def CanSum_slow(target_sum:int, number_list):
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for number in number_list:
        remainder = target_sum - number
        if(CanSum_stupid(remainder,number_list) == True):
            return True
    return False
```

As for this problem, we can dismantle it easily by using a memorization object. The run time
is now reduced to O(m*n), since the memo object has saved us lots of time going through duplicate values:

```python
def CanSum(target_sum:int, number_list,memo = None):
    if memo == None:
        memo = {}
    if target_sum in memo:
            return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for number in number_list:
        remainder = target_sum - number
        memo[remainder] = CanSum(remainder,number_list,memo)
        if memo[remainder] == True:
            return True
    return False
```