class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        res=0
        cache={}
        def dfs(i,j):
            nonlocal res
            if (i,j) in cache:
                return cache[i,j]
            if i>=len(s) or j>=len(t):
                if j>=len(t):
                    return 1
                return 0
            # skip the current one
            skip = dfs(i+1,j)
            # include the current one
            include = 0
            if s[i]==t[j]:
                include = dfs(i+1,j+1)
            cache[i,j] =  skip+include
            return cache[i,j]
        return dfs(0,0)