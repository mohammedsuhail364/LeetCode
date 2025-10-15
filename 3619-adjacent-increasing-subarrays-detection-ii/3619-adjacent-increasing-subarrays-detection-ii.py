class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        left=[1]*n #every index indicates length of longest increasing subarray end
        right=[1]*n #every index indicates length of longest increasing subarray start if it start from this index we have right[i] longest increasing subarray have
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                left[i]=left[i-1]+1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                right[i]=right[i+1]+1
        # to find the maximum possible value of k.
        res=0
        for i in range(n-1):
            adj_max=min(left[i],right[i+1])
            res=max(res,adj_max)
        return res