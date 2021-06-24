# This function will hold the memo dictionary object, used 
# for storing the result of the Unique_path function 

def Memorization(inner_function):
    memo = {}
    def save_memo_and_pass_param(column:int, row:int):
        #passing the key to the dictionary
        key = str(column) + ',' + str(row)
        if key not in memo:
            memo[key] = inner_function(column, row)
        return memo[key]
    return save_memo_and_pass_param

# Recursion function that calculate the number of unique paths
# from top left to bottom right. This function is warped by the
# Memorization decorator

@Memorization
def Unique_path_decorator(column:int, row:int):
    if(column == 1 and row == 1):
        return 1
    if(column == 0 or row == 0):
        return 0
    return Unique_path(column - 1,row) + Unique_path(column, row - 1)

# Same sollution but instead of using decorator function, 
# this function passes the memo object directly into its parameter

def Unique_path(column:int, row:int, memo_object = None):
    # Initialize the memo object if it is None
    if memo_object == None:
        memo_object = {}
    # Base cases
    if(column == 1 and row == 1):
        return 1
    if(column == 0 or row == 0):
        return 0
    #passing the key to the memo object (dictionary)
    key = str(column) + ',' + str(row)
    memo_object[key] = Unique_path(column - 1,row,memo_object) + Unique_path(column, row - 1,memo_object)
    #return a value if it has already been inside the memo object
    if key in memo_object:
        return memo_object[key]
    return memo_object[key]

# TESTING #

grid_test = [[0,0],[0,1],[1,0],[3,7],[10,10],[18,12],[31,38],[80,81]]

# It shouldn't take too long to perform these test

for grid in grid_test:
    print(Unique_path_decorator(grid[0],grid[1]))
    print(Unique_path(grid[0],grid[1],None))