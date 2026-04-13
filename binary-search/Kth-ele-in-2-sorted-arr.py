a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5

nums = []
i = 0
j = 0
while i<len(a) and j<len(b):
    if a[i]<=b[j]:
        nums.append(a[i])
        i+=1
    else:
        nums.append(b[j])
        j+=1
while i<len(a):
    nums.append(a[i])
    i+=1
while j<len(b):
    nums.append(b[j])
    j+=1
            
print(nums[k-1])    
    
    
            
    