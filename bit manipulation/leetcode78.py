# nums = [1,2,3]
# ans,Subset = [],[]
# def dfs(i):
#     if i>=len(nums):
#         print(Subset)
#         ans.append(Subset)
#         print(ans)
#         return
#     Subset.append(nums[i])
#     dfs(i+1)

#     Subset.pop()
#     dfs(i+1)
# dfs(0)
# print(ans)


# nums = [1, 2, 3]
# result,subset = [],[]
# def dfs(i):
#     if i>=len(nums):
#         result.append(subset.copy())
#         return
#     subset.append(nums[i])
#     dfs(i+1)

#     subset.pop()
#     dfs(i+1)
# dfs(0)
# print(result)

# by bit manipulation

nums = [1,2,3]
size = len(nums)
limit = (2**size)-1
i = 0
result = []
while i<=limit:
    subset = []
    j = 0
    k = i
    while k:
        bit_value = k%2
        if bit_value:
            subset.append(nums[j])
            print(subset)
        j += 1
        k>>=1
    result.append(subset.copy())
    print(result)
    i+=1
print(result)        
