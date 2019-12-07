'''
Reverse a given array
'''

def reverse_array(array):
    rev = []
    for _ in range(len(array)):
        rev.append(array.pop())
    return rev

test = [0, 1, 2, 6]
print(reverse_array(test))