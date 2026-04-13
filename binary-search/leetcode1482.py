bloomDay = [1,10,3,10,2]
m = 3
k = 1
if len(bloomDay)<m*k:
    print(-1)
min_days = max(bloomDay)
left = 1
right = max(bloomDay)
while left<=right:
    mid = (left+right)//2
    count_flower = 0
    count_bouquet = 0    
    for i in bloomDay:
        if i<=mid:
            count_flower +=1
            if count_flower==k:
                count_bouquet+=1
                count_flower = 0
        else:
            count_flower = 0
    if count_bouquet>=m:
        min_days = min(min_days,mid)
        right = mid-1
    else:
        left = mid+1
print(min_days)                    
