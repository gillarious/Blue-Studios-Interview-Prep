'''
Find the range of k in a sorted list. 

Ex. k = 3 and [0, 2, 3, 3, 3, 10, 10] => (2, 4)
Ex. k = 10 and [0, 2, 3, 3, 3, 10, 10] => (5, 6)
'''

def find_range(arr, target):
    start = find_start(arr, 0, len(arr) - 1, target)
    end = find_end(arr, start, len(arr) - 1, target)
    return (start, end)

def find_start(arr, start, end, target):
    distance = end - start
    midpoint = distance // 2 + start
    if arr[midpoint] == target:
        if midpoint == 0:
            return midpoint
        elif arr[midpoint - 1] < target:
            return midpoint
        return find_start(arr, start, midpoint, target)
    elif target < arr[midpoint]:
        return find_start(arr, start, midpoint - 1, target)
    elif target > arr[midpoint]:
        return find_start(arr, midpoint + 1, end, target)

def find_end(arr, start, end, target):
    distance = end - start
    midpoint = distance // 2 + start
    if arr[midpoint] == target:
        if midpoint == end:
            return midpoint
        elif arr[midpoint + 1] > target:
            return midpoint
        return find_end(arr, midpoint + 1, end, target)
    elif target < arr[midpoint]:
        return find_end(arr, midpoint + 1, end, target)
    elif target > arr[midpoint]:
        return find_end(arr, start, midpoint - 1, target)

test = [0, 2, 3, 3, 3, 10, 10]

k1 = 3
print(find_range(test, k1))

k2 = 10
print(find_range(test, k2))