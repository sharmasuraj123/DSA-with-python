def Heapify(arr, i, n):

    while i<n:
        largest = i
        left_child = 2*i+1
        right_child = 2 * i + 2
        if left_child<n and arr[largest]<arr[left_child]:
            largest = left_child

        if  right_child<n and arr[largest]<arr[right_child]:
            largest = right_child
        if largest == i:
            break
        else:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest


def BuildMaxHeap(arr):
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        Heapify(arr, i, n)

def HeapSort(arr):
    n = len(arr)
    while n>1:
        arr[0],arr[n-1] = arr[n-1],arr[0]
        n-=1
        Heapify(arr,0,n)
    
    
arr = [10, 3, 8, 9, 5, 13, 18, 14, 11]
BuildMaxHeap(arr)
HeapSort(arr)
print(arr)
