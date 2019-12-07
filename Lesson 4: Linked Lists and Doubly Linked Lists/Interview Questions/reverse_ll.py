'''
Write a function that reverses a linked list given the head of the list.

Ex. 1 -> 2 -> 3 -> 4 => 4 -> 3 -> 2 -> 1
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next

def reverse_ll(head):
    if head == None or head.next == None:
        return head
    curr = head
    while head.next != None:
        temp = head.next.next
        head.next.next = curr
        curr = head.next
        head.next = temp
    return curr

test = Node(1)
node_1 = Node(2)
node_2 = Node(3)
node_3 = Node(4)

test.next = node_1
node_1.next = node_2
node_2.next = node_3

test = reverse_ll(test)
print(test.traverse())