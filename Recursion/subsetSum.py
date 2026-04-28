arr = [1, 2, 1]
res = []
def Backtrack(idx,arr,curr,res):
    if idx==len(arr):
        res.append(curr)
        return 
    curr+=arr[idx]
    Backtrack(idx+1,arr,curr,res)
    curr-=arr[idx]
    Backtrack(idx+1,arr,curr,res)
Backtrack(0,arr,0,res)
print(res)    
    