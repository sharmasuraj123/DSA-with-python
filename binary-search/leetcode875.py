import math
piles = [3, 6, 7, 11]
h = 8
# find max = 11
max = 11
ans = max
for i in range(1,max+1):
    hour = 0
    for j in piles:
        hour += math.ceil(j/i)
    if hour<=h:
        print(j)
        break
    else:left = mid+1

# import math
# piles = [3, 6, 7, 11]
# h = 8
# sum = 0
# ans = 10**5
# for i in piles:
#     sum +=i
# left = 1
# right = sum
# while left<=right:
#     mid = (left+right)//2
#     hour = 0
#     for i in piles:
#       hour += math.ceil(i/mid)
#     if hour<=h:
#         ans = min(ans,mid)
#         right = mid-1
#     else:left = mid+1
# print(ans)
