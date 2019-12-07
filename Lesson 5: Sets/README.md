# Sets

### Initialization

```python
s = set()
```

### Runtime Analysis

| Function | Big O Complexity |
| --- | --- |
| length | O(1) |

```python
s = {0, 1, 2, 3, 4, 5}

len(s)
# returns 6
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| append           | O(1)             | 

```python
s = {0, 1, 2, 3, 4, 5}

s.add(6)
# s = {0, 1, 2, 3, 4, 5, 6}
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| remove           | O(1)             | 

```python
s = {0, 1, 2, 3, 4, 5}

s.remove(0)
# s = {1, 2, 3, 4, 5}
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| pop()            | O(1)             |

```python
s = {0, 1, 2, 3, 4, 5}

s.pop()
# returns 5
# s = {0, 1, 2, 3, 4}
```

| Function | Big O Complexity |
| --- | --- |
| equal to | O(N) |
| not equal to | O(N) |

```python
s = {0, 1, 2, 3, 4, 5}

s2 = {0, 1, 2, 3, 4, 5}
s == s2
# returns True

s3 = {0, 1, 2, 3, 4, 5, 6, 7}
s != s3
# returns True
```

| Function | Big O Complexity |
| --- | --- |
| iteration | O(N) |

```python
s = {0, 1, 2, 3, 4, 5}

for i in s:
    print(i, end=" ")
# returns 0 1 2 3 4 5
```