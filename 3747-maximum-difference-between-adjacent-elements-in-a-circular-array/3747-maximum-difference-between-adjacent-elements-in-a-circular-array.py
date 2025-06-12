class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res=float('-inf')
        for i in range(len(nums)-1):
            res=max(abs(nums[i]-nums[i+1]),res)
        res=max(abs(nums[-1]-nums[0]),res)
        return res