class Solution:
    def longestOnes(self, nums, k: int) -> int:
        zero=0
        l=0
        res=-inf
        for r in range(len(nums)):
            if not nums[r]:
                zero+=1
            while zero>k:
                if not nums[l]:
                    zero-=1
                l+=1
            res=max(res,(r-l+1))
        return res