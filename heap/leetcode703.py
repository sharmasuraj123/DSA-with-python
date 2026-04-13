import heapq
arr = [0]
heapq.heapify(arr)
res = heapq.nlargest(3,arr)
print(res)
heapq.heappush(arr,3)
res = heapq.nlargest(3, arr)
print(res)

heapq.heappush(arr, 5)
res = heapq.nlargest(3, arr)
print(res)

heapq.heappush(arr, 10)
res = heapq.nlargest(3, arr)
print(res)
