nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3
count,i,j,window_size = 0,0,-1,0
while i<len(nums):
    if nums[i]==0:
        count+=1
    i+=1
    
    while count>k:
        j+=1
        if nums[j]==0:
            count-=1
    window_size = max(window_size,i-j-1)
print(window_size)               
