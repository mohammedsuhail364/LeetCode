class Solution:
    def soupServings(self, n: int) -> float:
        if n>5000:
            return 1.0
        dp={}
        def dfs(a,b):
            if a<=0 and b<=0:
                return 0.5
            if a<=0 and b>0:
                return 1.0
            if a>0 and b<=0:
                return 0
            if (a,b) in dp:
                return dp[(a,b)]
            dp[(a,b)] =  0.25*(dfs(a-100,b)+dfs(a-75,b-25)+dfs(a-50,b-50)+dfs(a-25,b-75))
            return dp[(a,b)]
        return dfs(n,n)