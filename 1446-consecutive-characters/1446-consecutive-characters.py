class Solution:
    def maxPower(self, nums: str) -> int:
        res = 1
        cur = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                cur += 1
            else:
                cur = 1
            res = max(res, cur)
        return res