import heapq
arr = [12, 5, 787, 1, 23]
k = 2
heapq.heapify(arr)
max_heap = [-x for x in arr]
heapq.heapify(max_heap)
max_heap = [-x for x in max_heap]
print(heapq.nlargest(k,max_heap))
