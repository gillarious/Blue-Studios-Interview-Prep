'''
Implement a simple Queue class using only the stack data structure.
'''

class MyQueue:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
        self.size = 0

    def push(self, x: int) -> None:
        self.push_stack.append(x)
        self.size += 1
        
    def pop(self) -> int:
        if len(self.pop_stack) == 0:
            while len(self.push_stack) != 0:
                self.pop_stack.append(self.push_stack.pop())
        self.size -= 1
        return self.pop_stack.pop()
        
    def peek(self) -> int:
        if len(self.pop_stack) == 0:
            while len(self.push_stack) != 0:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]
        
    def empty(self) -> bool:
        return self.size == 0

test = MyQueue()    
test.push(1)        
test.push(2)        
print(test.peek())  # => 1 
print(test.pop())   # => 1
print(test.empty()) # => False
print(test.pop())   # => 2
print(test.empty()) # => True 