class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # worst question 
        dp=[[0]*k for i in range(k)]
        res=0
        for n in nums:
            cur=n%k
            for prev in range(k):
                dp[prev][cur]=dp[cur][prev]+1
                res=max(res,dp[prev][cur])
        return res