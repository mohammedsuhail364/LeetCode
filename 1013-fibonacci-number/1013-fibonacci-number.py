class Solution:
    
    def fib(self, n: int) -> int:
        memo={}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n<=1:
                return n
            res=dfs(n-1)+dfs(n-2)
            memo[n]=res
            return res
        return dfs(n)