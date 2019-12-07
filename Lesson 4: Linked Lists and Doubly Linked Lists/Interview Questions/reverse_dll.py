'''
Write a function that reverses a doubly linked list given the head of the list.

Ex. 1 <-> 2 <-> 3 <-> 4 => 4 <-> 3 <-> 2 <-> 1
'''

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

test = new DoublyLinkedList(1)