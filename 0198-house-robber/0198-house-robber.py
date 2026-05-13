class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        next1=0
        next2=0
        for i in range(n-1,-1,-1):
            cur=max(next1,nums[i]+next2)
            next2=next1
            next1=cur
        return next1