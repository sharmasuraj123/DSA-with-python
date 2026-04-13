class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next= next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def enqueue(self,new_element):
        new_node = Node(new_element)
        if not self.tail:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
        self.size+=1
    def isEmpty(self):
        return self.size==0

    def dequeue(self):
        if self.head is None:
            return "queue is empty"
        value = head.val
        head = head.next
        return value

    def peek(self):
        return self.head.val if self.head else "queue is empty"
    def length(self):
        return self.size

    def printQueue(self):
        curr = self.head
        while curr:
            print(curr.val,end=" ")
            curr = curr.next

myqueue = Queue()
print(myqueue.head)
print(myqueue.isEmpty())
print(myqueue.dequeue())
print(myqueue.peek())
myqueue.enqueue(5)
myqueue.enqueue(6)
print(myqueue.peek())
print(myqueue.length())
