class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        left=[1]*n # every index contains the longest increasing subarray ending this index
        right=[1]*n # every index contains the longest increasing subarray starting this index
        # it is essential to find because we can easily take the values of min(left[i],right(i+1)) it means i and i+1 are adjacent subarray we all know the values of both 
        for i in range(1,n):
            if nums[i] >nums[i-1]:
                left[i]=left[i-1]+1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                right[i]=right[i+1]+1
        res=0
        for i in range(n-1):
            adj=min(left[i],right[i+1])
            res=max(res,adj)
        return res