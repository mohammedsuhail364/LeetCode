class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def dfs(i):
            if i==n:
                return 1
            if i>n:
                return 0
            if i in memo:
                return memo[i]
            memo[i]=dfs(i+1)+dfs(i+2)
            return memo[i]
        return dfs(0)
