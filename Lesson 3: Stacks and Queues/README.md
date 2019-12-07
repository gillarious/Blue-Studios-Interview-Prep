# Stacks and Queues

## Stacks

### Initialization

```python
stack = []
```

### Runtime Analysis

| Function | Big O Complexity |
| --- | --- |
| size | O(1) |

```python
stack = [0, 1, 2, 3, 4, 5]

len(stack)
# returns 6
```

| Function | Big O Complexity |
| --- | --- |
| is empty | O(1) |

```python
stack = [0, 1, 2, 3, 4, 5]

len(stack) == 0
# returns False
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| peek           | O(1)             | 

```python
stack = [0, 1, 2, 3, 4, 5]

stack[-1]
# returns 5
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| push           | O(1)             | 

```python
stack = [0, 1, 2, 3, 4, 5]

stack.append(10)
# stack = [0, 1, 2, 3, 4, 5, 10]
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| pop            | O(1)             |

```python
stack = [0, 1, 2, 3, 4, 5]

stack.pop()
# returns 5
# stack = [0, 1, 2, 3, 4]
```

---

## Queues

### Initialization

```python
from collections import deque
queue = deque()
```

### Runtime Analysis

| Function | Big O Complexity |
| --- | --- |
| size | O(1) |

```python
queue = deque([0, 1, 2, 3, 4, 5])

len(queue)
# returns 6
```

| Function | Big O Complexity |
| --- | --- |
| is empty | O(1) |

```python
queue = deque([0, 1, 2, 3, 4, 5])

len(queue) == 0
# returns False
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| enqueue           | O(1)             | 

```python
queue = deque([0, 1, 2, 3, 4, 5])

queue.append(10)
# queue = deque([0, 1, 2, 3, 4, 5, 10])
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| dequeue            | O(1)             |

```python
queue = deque([0, 1, 2, 3, 4, 5])

queue.popleft()
# returns 0
# queue = deque([1, 2, 3, 4, 5])
```