class Solution:
    def fib(self, n: int) -> int:
        def dfs(n):
            if n==1 or n==0:
                return n
            return dfs(n-1)+dfs(n-2)
        return dfs(n)


