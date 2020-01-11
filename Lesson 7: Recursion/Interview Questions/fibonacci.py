'''
Generate the Fibonacci sequence up to k.
Here is the sequence up to 10 for reference:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

Ex. k = 0 => 0
Ex. k = 5 => 5
Ex. k = 10 => 55
'''

def fibonacci(k):
    if k == 0 or k == 1:
        return k
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)

k1 = 0
print(fibonacci(k1))

k2 = 5
print(fibonacci(k2))

k3 = 10
print(fibonacci(k3))