# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         nums.sort(key=lambda x:x-0)
#         return 
       
# class Solution:
    # def sortColors(self, nums: List[int]) -> None:
    #     c0,c1,c2 = 0,0,0

    #     for i in nums:
    #         if i == 0:
    #             c0+=1
    #         elif i == 1:
    #             c1 += 1
    #         else:
    #             c2 +=1      

    #     for i in range(c0):
    #         nums[i] = 0          
    #     for i in range(c0,c0+c1):
    #         nums[i] = 1 
    #     for i in range(c0+c1,len(nums)):
    #         nums[i] = 2   
    
    
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         left,right,idx = 0,len(nums)-1,0
#         while idx<=right:
#             if nums[idx]==0:
#                 nums[idx],nums[left] = nums[left],nums[idx]
#                 left+=1
#                 idx+=1
#             elif nums[idx]==2:
#                 nums[idx],nums[right] = nums[right],nums[idx]
#                 right-=1   
#             else:
#                 idx+=1   
#         return            
        
    