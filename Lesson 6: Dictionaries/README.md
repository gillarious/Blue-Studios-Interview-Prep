# Dictionaries

### Initialization

```python
d = {}
```

### Runtime Analysis

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| index            | O(1)             |
| index assignment | O(1)             |

```python
arr = [0, 1, 2, 3, 4, 5]

arr[1] 
# returns 1

arr[2] = 7 
# arr = [0, 1, 7, 3, 4, 5]
```

| Function | Big O Complexity |
| --- | --- |
| length | O(1) |

```python
arr = [0, 1, 2, 3, 4, 5]

len(arr)
# returns 6
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| append           | O(1)             | 

```python
arr = [0, 1, 2, 3, 4, 5]

arr.append(6)
# arr = [0, 1, 2, 3, 4, 5, 6]
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| insert           | O(N)             | 

```python
arr = [0, 1, 2, 3, 4, 5]

arr.insert(0, 10)
# arr = [10, 0, 1, 2, 3, 4, 5]
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| pop()            | O(1)             |
| pop(-1)          | O(1)             |
| pop(i)           | O(N)             |

```python
arr = [0, 1, 2, 3, 4, 5]

arr.pop()
# returns 5
# arr = [0, 1, 2, 3, 4]

arr.pop(-1)
# returns 5
# arr = [0, 1, 2, 3, 4]

arr.pop(3)
# returns 3
# arr = [0, 1, 2, 4, 5]
```

| Function | Big O Complexity |
| --- | --- |
| equal to | O(N) |
| not equal to | O(N) |

```python
arr = [0, 1, 2, 3, 4, 5]

arr2 = [0, 1, 2, 3, 4, 5]
arr == arr2
# returns True

arr3 = [0, 1, 2, 3, 4, 5, 6, 7]
arr != arr3
# returns True
```

| Function | Big O Complexity |
| --- | --- |
| iteration | O(N) |

```python
arr = [0, 1, 2, 3, 4, 5]

for keys in d.keys():
    print(i, end=" ")
# returns 0 1 2 3 4 5

for vals in arr:
    print(i, end=" ")
# returns 0 1 2 3 4 5

for i in arr:
    print(i, end=" ")
# returns 0 1 2 3 4 5
```