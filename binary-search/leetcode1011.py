weights = [1, 2, 3, 1, 1]
days = 4
total = sum(weights)
left = max(weights)
right = total
min_days = total
while left<=right:
    mid = (left+right)//2
    capicity_sum = 0
    count_days = 0
    i = 0
    while i<len(weights):
        capicity_sum+=weights[i]
        if capicity_sum==mid:
            count_days+=1
            capicity_sum = 0
        elif capicity_sum>mid:
            count_days +=1
            i-=1
            capicity_sum = 0
        i+=1    
    if capicity_sum>0:
        count_days+=1
    if count_days<=days:
        min_days = min(min_days,mid)
        right = mid-1
    else:
        left = mid + 1
print(min_days)
