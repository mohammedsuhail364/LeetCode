from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #  find the prefix multiplication
        prefix=1 # default case when i = 0 
        res=[0]*len(nums)
        for i in range(len(nums)):
            res[i]=prefix
            prefix=prefix*nums[i]
        
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*suffix
            suffix=suffix*nums[i]
        return res