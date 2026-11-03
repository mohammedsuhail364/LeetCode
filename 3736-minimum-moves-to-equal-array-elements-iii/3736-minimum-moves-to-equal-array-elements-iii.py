class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_val = max(nums)
        res = sum(max_val - x for x in nums)
        return res