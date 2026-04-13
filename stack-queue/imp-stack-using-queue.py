# from queue import Queue
# stack = Queue()
# stack.put(4)
# stack.put(5)
# stack.put(6)
# stack.put(7)
# print(stack.get())
# print(stack.qsize())


from queue import Queue


class MyStack:

    def __init__(self):
        self.stack = Queue()

    def push(self, x: int) -> None:
        self.stack.put(x)
        return

    def pop(self) -> int:
        size = self.stack.qsize()
        i = 1
        while i < size:
            self.stack.put(self.stack.get())
            i += 1
        return self.stack.get()

    def top(self) -> int:
        size = self.stack.qsize()
        i = 1
        while i < size:
            self.stack.put(self.stack.get())
            i += 1
        top_ele = self.stack.get()
        self.stack.put(top_ele)
        return top_ele

    def empty(self) -> bool:
        return self.stack.empty()


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(55)
obj.push(67)
obj.push(99)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2,param_3,param_4)
