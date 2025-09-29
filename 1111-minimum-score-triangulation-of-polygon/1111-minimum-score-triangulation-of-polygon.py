class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # refer this https://www.youtube.com/watch?v=rSOpBCPZlqY
        n=len(values)
        memo={}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[i,j]
            if (j-i<=1):
                return 0
            if j-i==2:
                return values[i]*values[j]*values[i+1]
            
            res=inf
            for k in range(i+1,j):
                res=min(res,dfs(i,k)+(values[i]*values[j]*values[k])+dfs(k,j))
            memo[i,j]=res
            return res
        return dfs(0,n-1)

                    