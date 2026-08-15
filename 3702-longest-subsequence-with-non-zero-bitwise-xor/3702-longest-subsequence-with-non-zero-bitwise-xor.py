class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if all(num == 0 for num in nums):
            return 0
        xor=0
        for n in nums:
            xor=xor^n
        n=len(nums)
        if xor != 0:
            return n
        return n-1