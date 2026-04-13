n = 1
left = 1
right = n 
ans = 1
while left <=right:
    mid = (left+right)//2
    if mid*mid==n:
        print(mid)
        break
    elif mid*mid>n:
        right = mid-1
    else:
        ans = mid
        left = mid+1
        
print(ans)        
