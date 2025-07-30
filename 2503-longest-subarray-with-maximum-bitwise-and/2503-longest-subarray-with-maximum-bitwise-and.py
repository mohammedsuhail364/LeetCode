class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        size=0
        res=0
        target=max(nums)
        for num in nums:
            if num==target:
                size+=1
            else:
                size=0
            res=max(size,res)
        
        return res

        