class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i,v in enumerate(nums):
            if n%(i+1)==0:res+=(v*v)
        return res