class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[[inf]*(r+1) for r in range(len(triangle)+1)]
        ROWS=len(triangle)
        # base case
        for c in range(len(triangle[ROWS-1])):
            dp[ROWS-1][c]=triangle[ROWS-1][c]
        for r in range(ROWS-1,-1,-1):
            if r==ROWS-1:
                continue
            for c in range(len(triangle[r])-1,-1,-1):
                dp[r][c]=triangle[r][c]+min(dp[r+1][c+1],dp[r+1][c])
        return dp[0][0]
        # ROWS=len(triangle)
        # cache={}
        # def dfs(r,c):
        #     if (r,c) in cache:
        #         return cache[r,c]
        #     if r>=ROWS:
        #         return inf
        #     if c<0 or c>=len(triangle[r]):
        #         return inf
        #     if r==ROWS-1:
        #         return triangle[r][c]
        #     cache[r,c] = triangle[r][c]+min(dfs(r+1,c+1),dfs(r+1,c))
        #     return cache[r,c]
        # return dfs(0,0)