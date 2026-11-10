class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        memo = {}
        def dfs(i):
            if(i) in memo:return memo[i]
            if i==n:
                return 0
            res=inf
            for k in (1,2,3):
                j=i+k
                if j<=n:
                    res=min(res,costs[j-1]+(k*k)+dfs(j))
            memo[i] = res
            return res
            
        return dfs(0)
