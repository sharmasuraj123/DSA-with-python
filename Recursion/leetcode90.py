nums = [1, 2, 2]
nums.sort()
res = []

def Backtrack(idx, nums, curr, res):

    res.append(curr.copy())
    prev = None
    for i in range(idx,len(nums)):
        if prev is not None and nums[i]==prev:
            continue
        curr.append(nums[i])
        Backtrack(i + 1, nums, curr, res)
        curr.pop()

        prev = nums[i]


Backtrack(0, nums, [], res)
print(res)


# nums = [1, 2, 2]
# res = set()
# nums.sort()
# def Backtrack(idx, nums, curr, res):
#     if idx == len(nums):
#         res.add(tuple(curr))
#         return
#     curr.append(nums[idx])
#     Backtrack(idx + 1, nums, curr, res)
#     curr.pop()
#     Backtrack(idx + 1, nums, curr, res)

# Backtrack(0, nums, [], res)
# unique = [list(sub) for sub in res]
# print(unique)


