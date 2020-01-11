# Binary Search Trees

### Initialization

```python
class Node:
    def __init__(self, val): 
        self.val = val  
        self.left = None  
        self.right = None 

    def __str__(self):
        return str(self.val) 

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
```

### Runtime Analysis

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| traversal | O(N) |

## Depth First Traversal

### Pre Order Traversal Implementation

```python
def preorder(root):
    if root == None:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)
```

### In Order Traversal Implementation

```python
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)
```

### Post Order Traversal Implementation

```python
def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")
```

## Breadth First Traversal

### Implementation

```python
def levelorder(root):
    this_level = [root]
    while len(this_level) != 0:
        next_level = []
        for node in this_level:
            print(node, end=" ")
            if node.left != None:
                next_level.append(node.left)
            if node.right != None:
                next_level.append(node.right)
        this_level = next_level
```