# n = 3.         ## O(1)time complexity but using built in function that is not good
# m = 8
# x = m**(1/n)
# if (int(x)==x):
#     print(int(x))
# else:
#     print(-1) 

n = 3
m = 8
left = 1
right = m
while left<=right:
    mid = (left+right)//2
    ans = 1
    for i in range(n):
        ans*=mid
        if ans>m:
            break
        
    if ans == m:
        print(mid)
        break
    elif ans>m:
        right = mid-1
    else:
        left = mid+1
        
print(-1)          
           