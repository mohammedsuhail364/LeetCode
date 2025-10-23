class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def dfs(i):
            if i==n:
                return 1
            if i>=n:
                return 0
            return dfs(i+1)+dfs(i+2)
        return dfs(0)