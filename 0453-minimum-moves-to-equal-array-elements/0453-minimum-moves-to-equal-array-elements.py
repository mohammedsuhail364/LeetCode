class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n=len(nums)
        min_val = min(nums)
        heapq.heapify_max(nums)
        res=0
        while nums[0]!=min_val:
            x=heappop_max(nums)
            c = x-min_val
            heappush_max(nums,min_val)
            res+=c
        return res