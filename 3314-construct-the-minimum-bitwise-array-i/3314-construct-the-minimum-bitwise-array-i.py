from typing import List
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res=[-1]*len(nums)
        for i in range(len(nums)):
            target=nums[i]
            x=1
            while x<1001: 
                if (x | (x + 1) )==target:
                    res[i]=x
                    break
                x+=1
        return res