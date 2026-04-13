class Stack:
    def __init__(self):
        self.List = []

    def push(self,new_element):
        self.List.append(new_element)

    def isEmpty(self):
        return len(self.List) == 0

    def pop(self):
        return self.List.pop() if not self.isEmpty() else "stack is empty" 
     
    def peek(self):
        return self.List[-1] if not self.isEmpty() else "stack is empty" 
    
    def size(self):
        return len(self.List)

mystack = Stack()
print(mystack.isEmpty())
mystack.push(4)
print(mystack.isEmpty())
mystack.push(6)
print(mystack.peek())
print(mystack.size())
print(mystack.pop())
print(mystack.size())
