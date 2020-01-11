'''
Write a function that finds the height of a binary search tree.

Ex.  3
   /   \
  2     5
 /     / \
1     4   6
           \
            7
height => 3
'''

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

tree = BinarySearchTree()
test = [3, 5, 2, 1, 4, 6, 7]

for i in range(len(test)):
    tree.insert(test[i])

def height(root):
    if root == None:
        return 0
    else:
        return search(root, 0)
    
def search(curr, count):
    if curr.left != None and curr.right != None:
        return max(search(curr.left, count+1), search(curr.right, count+1))
    elif curr.left == None and curr.right != None:
        return search(curr.right, count+1)
    elif curr.right == None and curr.left != None:
        return search(curr.left, count+1)
    else:
        return count

print(height(tree.root))

def recursive_height(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 0
    return 1 + (recursive_height(root.left) if recursive_height(root.left) >= recursive_height(root.right) else recursive_height(root.right))

print(recursive_height(tree.root))