arr =  [1, 1, 2, 2, 2, 2, 3]
target = 2

def binarySearch(arr,target,leftbiased):
    left = 0 
    right = len(arr)-1
    ans = -1
    while left<=right:
        mid = (left+right)//2
        if arr[mid]>target:
            right = mid - 1
        elif arr[mid]<target:

            left = mid+1
        else:
            ans = mid
            if leftbiased:
                right = mid-1
            else:
                left = mid+1
    return ans

leftidx = binarySearch(arr,target,True)
rightidx = binarySearch(arr,target,False) 
print(rightidx-leftidx+1)                      
