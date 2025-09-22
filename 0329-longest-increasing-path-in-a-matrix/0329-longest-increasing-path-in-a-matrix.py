class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        dp=[[0]*cols for _ in range(rows)]
        def dfs(r,c):
            if dp[r][c]!=0:
                return dp[r][c]
            best=1
            for nr,nc in [(r,c-1),(r,c+1),(r-1,c),(r+1,c)]:
                if 0<=nr<rows and 0<=nc<cols and matrix[nr][nc]>matrix[r][c]:
                    best=max(best,1+dfs(nr,nc))
            dp[r][c]=best  
            return best
        res=0
        for r in range(rows):
            for c in range(cols):
                res=max(res,dfs(r,c))
        return res