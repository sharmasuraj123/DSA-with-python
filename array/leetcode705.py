class MyHashSet:

    def __init__(self):
        self.size = 1
        self.buckets = [[] for _ in range(self.size)]


obj = MyHashSet()
print(obj.buckets)