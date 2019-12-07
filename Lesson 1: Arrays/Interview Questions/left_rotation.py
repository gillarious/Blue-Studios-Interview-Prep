'''
Rotate an array to the left k amount of times
Ex. k = 4 so [1, 2, 3, 4, 5] => [5, 1, 2, 3, 4]
'''

def rotate_left(array, k):
    return array[k % len(array):] + array[0:k % len(array)]

test = [1, 2, 3, 4, 5]
print(rotate_left(test, 4))