'''
Write a function that reverses a doubly linked list given the head of the list.

Ex. 1 <-> 2 <-> 3 <-> 4 => 4 <-> 3 <-> 2 <-> 1
'''

class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

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

def reverse_dll(head):
    if head == None or head.next == None:
        return head
    curr = head
    while curr != None:
        temp = curr.prev  
        curr.prev = curr.next
        curr.next = temp 
        head = curr
        curr = curr.prev
    return head

test = DoublyNode(1)
node_1 = DoublyNode(2)
node_2 = DoublyNode(3)
node_3 = DoublyNode(4)

test.next = node_1
node_1.next = node_2
node_1.prev = test
node_2.next = node_3
node_2.prev = node_1
node_3.prev = node_2

test = reverse_dll(test)
print(test.traverse_right())