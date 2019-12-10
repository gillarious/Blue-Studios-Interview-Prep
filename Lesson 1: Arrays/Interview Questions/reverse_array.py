'''
Reverse a given array.

Ex. [0, 1, 2, 6] => [6, 2, 1, 0]
'''

def reverse_array(array):
    rev = []
    for _ in range(len(array)):
        rev.append(array.pop())
    return rev

def reverse(array):
    return array[::-1]

def reverse2(array):
    return list(reversed(array))

test = [0, 1, 2, 6]
#print(reverse_array(test))

print(reverse2(test))