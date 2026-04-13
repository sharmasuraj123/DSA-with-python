class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


class Stack():
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,new_element):
        new_node = Node(new_element)
        if self.head:new_node.next = self.head
        self.head = new_node
        self.size+=1
    def pop(self):
        value = self.head.val if self.head else "stack is empty"
        self.head = self.head.next if self.head else None  
        self.size-=1
        return value

    def isEmpty(self):
        return self.size==0

    def peek(self):
        return self.head.val if self.head else "stack is empty"

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.val,end="->")
            curr = curr.next
        print()

mystack = Stack()
print(mystack.isEmpty())
mystack.push(4)
print(mystack.isEmpty())
mystack.push(6)
print(mystack.peek())
print(mystack.size)
print(mystack.pop())
print(mystack.size)
mystack.traverse()
