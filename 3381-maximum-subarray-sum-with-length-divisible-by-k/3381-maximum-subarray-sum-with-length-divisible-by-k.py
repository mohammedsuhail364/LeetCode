class Solution:
    def maxSubarraySum(self, nums, k: int) -> int:
        # refer neetcode
        min_sum=[float('inf')]*k
        min_sum[0]=0 # refer empty sub array
        res=float("-inf")
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            length=i+1
            subtract=min_sum[length%k]
            temp=total-subtract
            res=max(res,temp)
            min_sum[length%k]=min(min_sum[length%k],total)
        return res