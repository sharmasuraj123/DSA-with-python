# brute force by dictionary 
# class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     result,count = 0,0
    #     hashmap = {}
    #     for i in nums:
    #         hashmap[i] = 1 + hashmap.get(i,0)
    #         if hashmap[i]>count:
    #             result = i
    #         count = max(hashmap[i],count)

    #     return result        



# nums = [2,2,1,1,1,2,2]
# count = 1
# major = nums[0]
# for i in range(1,len(nums)):
#     if count==0:
#         major=nums[i]
#         count+=1
#     elif nums[i]==major:
#         count+=1
#     else:
#         count-=1
# print(major)    

    