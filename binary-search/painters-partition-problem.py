arr = [100, 200, 300, 400]
k = 1
total = sum(arr)
left = max(arr)
right = total
min_time = total
while left<=right:
    mid = (left+right)//2
    cout_painter = 0
    i = 0
    unit_work = 0
    while i<len(arr):
        unit_work+=arr[i]
        if unit_work == mid:
            cout_painter+=1
            unit_work = 0
        elif unit_work>mid:
            cout_painter+=1
            unit_work = 0
            i-=1
        i+= 1
    if unit_work>0:cout_painter+=1    
    if cout_painter<=k:
        min_time = min(min_time,mid)
        right = mid-1
    else:left = mid+1         
print(min_time)          
