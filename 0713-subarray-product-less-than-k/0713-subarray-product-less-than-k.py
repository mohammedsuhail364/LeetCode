class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if k <= 1:  # important edge case
            return 0
        cur_sum=1
        l=0
        res=0
        for r in range(len(nums)):
            cur_sum=cur_sum*nums[r]
            while cur_sum>=k and l<len(nums):
                cur_sum=cur_sum/nums[l]
                l+=1
            res+=(r-l+1)
        return res 