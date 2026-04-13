arr = [4,2,7,6,9]
arr.sort()
Cost,sum = 0,0
while len(arr)>1:
    a = arr[0] 
    b = arr[1] 
    sum = a + b
    Cost+=sum
    arr.append(sum)
    arr.pop(0)
    arr.pop(0)
    arr.sort()
print(Cost )
