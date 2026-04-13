class Queue:
    def __init__(self):
        self.List = []

    def enqueue(self,new_element):
        self.List.append(new_element)

    def isEmpty(self):
        return len(self.List)==0

    def dequeue(self):
        return self.List.pop(0) if not self.isEmpty() else "queue is empty"

    def peek(self):
        return self.List[0] if not self.isEmpty() else "queue is empty"
    
    def size(self):
        return len(self.List)
    
myqueue = Queue()    
print(myqueue.List)
print(myqueue.isEmpty())
print(myqueue.dequeue())
myqueue.enqueue(5)
myqueue.enqueue(6)
print(myqueue.peek())
print(myqueue.size())