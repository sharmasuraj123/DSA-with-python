import heapq
arr = [4,53,5,25,37]
heapq.heapify(arr)
temp = arr.copy()
while temp:
    pop_ele = heapq.heappop(temp)
    print(pop_ele)

heapq.heappush(arr,45)    
heapq.heappush(arr, 85) # 4,5,25,37,45,53,85
print(arr[0],len(arr))
heapq.heappushpop(arr,8)
temp = arr.copy()
while temp:
    print(heapq.heappop(temp))
heapq.heapreplace(arr,7)
nlargest = heapq.nlargest(4,arr)
print(nlargest)


# heapq.heappush(pq, (priority, value)).  // priority queue in tuples
