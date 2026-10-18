class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9+7
        def count(nums):
            if not nums:return 1
            root = nums[0]
            left = [l for l in nums if l < root]
            right = [r for r in nums if r > root]
            return math.comb(len(nums)-1,len(left))*count(left)%MOD*count(right)%MOD
        return count(nums) - 1%MOD