'''
You are located at the top-left corner of a MxN grid. You can only move either down or 
right at any point in time. You are trying to reach the bottom-right corner of the grid. 
How many unique paths are there?

Ex. M = 3 and N = 3 => 6
Ex. M = 5 and N = 5 => 70
'''

def number_of_paths(m, n):
    if m == 0 or n == 0:
        return 0
    elif m == 1 or n == 1:
        return 1
    else:
        return number_of_paths(m-1, n) + number_of_paths(m, n-1)

m1 = 3
n1 = 3
print(number_of_paths(m1, n1))

m2 = 5
n2 = 5
print(number_of_paths(m2, n2))