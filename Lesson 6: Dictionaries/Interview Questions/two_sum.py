'''
Given a list of numbers and a number k, determine whether or not any two numbers from the list add up to k.

Ex. k = 17 so [10, 15, 3, 7] => True
Ex. k = 22 so [14, 17, 1, 9] => False
Ex. k = 9 so [2, 7, 11, 15] => True
'''

def two_sum(arr, k):
    nums = {}
    for i in arr:
        if i not in nums:
            nums[i] = k - i
        if i in nums.values():
            return True
    return False
        
test1 = [10, 15, 3, 7]
k1 = 17
print(two_sum(test1, k1))

test2 = [14, 17, 1, 9]
k2 = 22
print(two_sum(test2, k2))

test3 = [2, 7, 11, 15]
k3 = 9
print(two_sum(test3, k3))