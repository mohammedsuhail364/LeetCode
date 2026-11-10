class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [inf]*(n+1)
        dp[n]=0
        for i in range(n-1,-1,-1):
            res=inf
            for k in (1,2,3):
                j=i+k
                if j<=n:
                    res=min(res,costs[j-1]+(k*k)+dp[j])
            dp[i]=res
        return dp[0]
