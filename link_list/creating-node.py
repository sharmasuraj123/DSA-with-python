class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

# Create a object.
a = Node(67)
b = Node(77)
b.data = 85
print(a)
print(a.next)
a.next = b
print(a.data)
pointer = a
pointer = pointer.next
print(pointer.data)       
    
  