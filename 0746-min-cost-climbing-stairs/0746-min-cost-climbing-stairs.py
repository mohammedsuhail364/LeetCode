class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[0]*(n+2)
        for i in range(n-1,-1,-1):
            one_step=dp[i+1]
            two_step=dp[i+2]
            dp[i]=cost[i]+min(one_step,two_step)
        return min(dp[0],dp[1])
