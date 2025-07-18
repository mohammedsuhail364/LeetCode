class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        dp={}
        n=len(cost)
        def backtrack(i):
            if i>=n:
                return 0
            if i in dp:
                return dp[i]
            c1=cost[i]+ backtrack(i+1)
            c2=cost[i]+backtrack(i+2)
            dp[i]=min(c1,c2)
            return dp[i]
        c1=backtrack(0)
        c2=backtrack(1)
        return min(c1,c2)