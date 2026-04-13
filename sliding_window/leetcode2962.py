    # def countSubarrays(self, nums: List[int], k: int) -> int:
    #     max_ele = max(nums)
    #     l,r,count,n = 0,0,0,len(nums)
    #     total = 0
    #     while r<n:
    #         if nums[r] == max_ele:
    #             count+=1
    #         while count>=k:
    #             total+=(n-r)
    #             if nums[l]==max_ele:
    #                 count-=1
    #             l+=1
    #         r+=1
    #     return total 