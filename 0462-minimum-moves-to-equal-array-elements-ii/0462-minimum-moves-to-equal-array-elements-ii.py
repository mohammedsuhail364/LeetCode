class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        res=0
        if len(nums)%2:
            mid = len(nums)//2
            t = nums[mid]
            for n in nums:
                res += abs(n-t)
        else:
            mid = len(nums)//2
            t = nums[mid]
            for n in nums:
                res += abs(n-t)
            res1 = 0
            t = nums[mid-1]
            for n in nums:
                res1 += abs(n-t)
            res = min(res,res1)
        return res

