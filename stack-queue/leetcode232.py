from queue import LifoQueue
class MyQueue:
    def __init__(self):
        self.queuee = LifoQueue()
        self.temp_st = LifoQueue()
        self.size = 0 

    def push(self, x: int) -> None:
        self.queuee.put(x)
        self.size += 1

    def pop(self) -> int:
        i = 1
        while i<self.size:
            self.temp_st.put(self.queuee.get())
            i+=1
        pop_num = self.queuee.get()
        while not self.temp_st.empty():  
            self.queuee.put(self.temp_st.get())
        return pop_num    

    def peek(self) -> int:
        i = 1
        while i < self.size:
            self.temp_st.put(self.queuee.get())
            i += 1
        peek_num = self.queuee.get()
        self.queuee.put(peek_num)
        while not self.temp_st.empty():
            self.queuee.put(self.temp_st.get())
        return peek_num    

    def empty(self) -> bool:
        return self.queuee.empty()
