class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+2)
        dp[n]=1
        for step in range(n-1,-1,-1):
            dp[step]=dp[step+1]+dp[step+2]
        return dp[0]
