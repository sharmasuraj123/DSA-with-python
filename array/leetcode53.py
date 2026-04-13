nums = [5, 4, -1, 7, 8]
sum = 0
max_sum = -10000000
for i in nums:
    sum += i
    max_sum = max(max_sum,sum)
    if sum<0:
        sum = 0
print(max_sum)        
