'''
Reverse a given array.

Ex. [0, 1, 2, 6] => [6, 2, 1, 0]
'''

def reverse_array(array):
    rev = []
    for _ in range(len(array)):
        rev.append(array.pop())
    return rev

test = [0, 1, 2, 6]
print(reverse_array(test))