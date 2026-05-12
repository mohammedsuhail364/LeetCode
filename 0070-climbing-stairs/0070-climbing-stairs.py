class Solution:
    def climbStairs(self, n: int) -> int:
        cache={}
        def dfs(step):
            if step in cache:
                return cache[step]
            if step>n:
                return 0
            if step==n:
                return 1
            cache[step] = dfs(step+1)+dfs(step+2)
            return cache[step]
        return dfs(0)