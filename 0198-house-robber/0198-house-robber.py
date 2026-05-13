class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n+2)
        dp[n-1]=nums[n-1]
        for i in range(n-1,-1,-1):
            skip=dp[i+1]
            include=nums[i]+dp[i+2]
            dp[i]=max(skip,include)
        return dp[0]