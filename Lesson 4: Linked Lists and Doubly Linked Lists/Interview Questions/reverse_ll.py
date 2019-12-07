'''
Write a function that reverses a linked list given the head of the list.

Ex. 1 -> 2 -> 3 -> 4 => 4 -> 3 -> 2 -> 1
'''

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

test = new LinkedList(1)