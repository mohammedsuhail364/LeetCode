class Solution:
    def minCut(self, s: str) -> int:
        # refer striver
        cache={}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i>=len(s):
                return 0
            cache[i]=inf
            temp=""
            for j in range(i,len(s)):
                temp+=s[j]
                if temp==temp[::-1]:
                    cost=1+dfs(j+1)
                    cache[i]=min(cost,cache[i])
            return cache[i]

        return dfs(0)-1