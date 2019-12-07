'''
Rotate an array to the right k amount of times
Ex. k = 4 so [1, 2, 3, 4, 5] => [2, 3, 4, 5, 1]
'''

def rotate_right(array, k):
    if len(array) == 0:
        return array
    for _ in range(k):
        temp = array[-1]
        for i in range(len(array)-1, 0, -1):
            array[i] = array[i-1]
        array[0] = temp
    return array

test = [1, 2, 3, 4, 5]
print(rotate_right(test, 4))
