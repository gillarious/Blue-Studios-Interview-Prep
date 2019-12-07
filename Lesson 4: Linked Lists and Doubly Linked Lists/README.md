# Linked Lists and Doubly Linked Lists

## Linked Lists

### Initialization

```python
class LinkedList:
    def __init__(self, head):
        self.head = head

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
```

### Runtime Analysis

| Function | Big O Complexity |
| --- | --- |
| length | O(N) |
| insert      | O(1)   | 
| delete      | O(1)     | 
| iteration | O(N) |

```python
def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next
```

---

## Doubly Linked Lists

### Initialization

```python
class DoublyLinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
```

### Runtime Analysis

| Function | Big O Complexity |
| --- | --- |
| length | O(N) |
| insert left           | O(1)   | 
| insert right           | O(1)   | 
| delete          | O(1)     | 
| iteration | O(N) |

```python
def traverse_right(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next

def traverse_left(self):
        node = self
        while node != None:
            print(node.val)
            node = node.prev
```