import heapq
arr = [1,2,3,4]
N = 4


# def heapify(self,arr, i, n):
#         while i<n:
#             largest = i
#             left_child = 2*i+1
#             right_child = 2 * i + 2
#             if left_child<n and arr[largest]<arr[left_child]:
#                 largest = left_child

#             if  right_child<n and arr[largest]<arr[right_child]:
#                 largest = right_child
#             if largest == i:
#                 break
#             else:
#                 arr[i], arr[largest] = arr[largest], arr[i]
#                 i = largest
#     def convertMinToMaxHeap(self, N, arr):
#         for i in range((N // 2) - 1, -1, -1):
#             self.heapify(arr, i, N)
#         return arr


# heapq.heapify(arr)

# Convert to max-heap
max_heap = [-x for x in arr]
heapq.heapify(max_heap)
maxi = [-x for x in max_heap]
print(maxi)
