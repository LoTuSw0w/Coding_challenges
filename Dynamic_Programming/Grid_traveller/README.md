# QUESTIONS:
(Source: [___LEETCODE___](https://leetcode.com/problems/unique-paths/)) 
 
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

EXAMPLE:
```
Input: m = 3, n = 7
Output: 28
```

# How I solve it:

Normally, a question like this can be solve recursively, just like this:

```python
def Unique_path(column:int, row:int):
    if(column == 1 and row == 1):
        return 1
    if(column == 0 or row == 0):
        return 0
    return Unique_path(column - 1,row) + Unique_path(column, row - 1)
```

However, this approach is not very efficient. Since each instance of this function will span 2 additional instances, as a result, the run time complexity of this would be ~O(2^n), which is huge and unacceptable!

To reduce the run time of this function, we can use a memorization object to store the unique value generated by an instance of this function, so we don't have to execute it again. In python, we can achieve this using a function decorator. The runtime of this method is now reduced to O(n).

```python
def Memorization(inner_function):
    memo = {}
    def save_memo_and_pass_param(column:int, row:int):
        key = str(column) + ',' + str(row)
        if key not in memo:
            memo[key] = inner_function(column, row)
        return memo[key]
    return save_memo_and_pass_param
```