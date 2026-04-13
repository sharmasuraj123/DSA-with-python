def Heapify(arr, i, n):  # space complexity:-O(n)with recursion and O(1) in while loop
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and arr[largest] < arr[left_child]:  # sign change and minheap.
        largest = left_child
    if right_child < n and arr[largest] < arr[right_child]:  # sign change and minheap.
        largest = right_child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        Heapify(arr, largest, n)

    # while i<n:
    #     largest = i
    #     left_child = 2*i+1
    #     right_child = 2 * i + 2
    #     if left_child<n and arr[largest]<arr[left_child]:
    #         largest = left_child

    #     if  right_child<n and arr[largest]<arr[right_child]:
    #         largest = right_child
    #     if largest == i:
    #         break
    #     else:
    #         arr[i], arr[largest] = arr[largest], arr[i]
    #         i = largest


def BuildMaxHeap(arr):
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        Heapify(arr, i, n)


arr = [10, 3, 8, 9, 5, 13, 18, 14, 11, 70]
BuildMaxHeap(arr)
print(arr)
