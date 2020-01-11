# Dictionaries

### Initialization

```python
d = {}

from collections import defaultdict
d = defaultdict(list) 
```

### Runtime Analysis

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| index            | O(1)             |

```python
d = {"apples": 3, "oranges": 1, "strawberries": 10}

d["apples"] 
# returns 3
```

| Function | Big O Complexity |
| --- | --- |
| length | O(1) |

```python
d = {"apples": 3, "oranges": 1, "strawberries": 10}

len(d)
# returns 3
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| store            | O(1)             |

```python
d = {"apples": 3, "oranges": 1, "strawberries": 10}

d["apples"] = 5
# d = {"apples": 5, "oranges": 1, "strawberries": 10}

d["bananas"] = 2
# d = {"bananas": 2, "apples": 5, "oranges": 1, "strawberries": 10}
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| del          | O(1)             | 

```python
d = {"apples": 3, "oranges": 1, "strawberries": 10}

del d["apples"]
# d = {"oranges": 1, "strawberries": 10}
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| popitem()            | O(1)             |
| pop(k)           | O(1)             |

```python
d = {"apples": 3, "oranges": 1, "strawberries": 10}

d.popitem()
# returns 3
# d = {"oranges": 1, "strawberries": 10}

d.pop("oranges")
# returns 1
# d = {"strawberries": 10}
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| clear         | O(1)             | 

```python
d = {"apples": 3, "oranges": 1, "strawberries": 10}

d.clear()
# d = {}
```

| Function | Big O Complexity |
| --- | --- |
| iteration | O(N) |

```python
d = {"apples": 3, "oranges": 1, "strawberries": 10}

for keys in d.keys():
    print(keys, end=" ")
# returns apples oranges strawberries

for vals in d.values():
    print(vals, end=" ")
# returns 3 1 10

for keys, vals in d.items():
    print(keys + " " + str(vals), end=" ")
# returns apples 3 oranges 1 strawberries 10
```