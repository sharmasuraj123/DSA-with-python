class MaxHeap:
    heap = []
    size = 0
    def __init__(self,length):
        self.length = length

    def insert(self,value):
        if self.size>=self.length:
            print("heap is full") 
            return
        else:
            self.heap.append(value)
            self.size+=1

        # position the last element

        i = (self.size-1)
        while i > 0 and self.heap[(i - 1) // 2] < self.heap[i]:
            self.heap[(i - 1) // 2], self.heap[i] = self.heap[i],self.heap[(i-1) // 2]
            i = (i - 1) // 2
    

obj = MaxHeap(4)
obj.insert(5)
obj.insert(25)
obj.insert(15)
obj.insert(54)
obj.insert(56)
print(MaxHeap.heap)
