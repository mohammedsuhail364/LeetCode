class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        dp={}
        def backtrack(r,c):
            if (r,c)==(rows-1,cols-1):
                return 1
            if (r,c) in dp:
                return dp[(r,c)]
            grid[r][c]=-1
            paths=0
            for nr,nc in [(r+1,c),(r,c+1)]:
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==0:
                    paths+=backtrack(nr,nc)
            grid[r][c]=0
            dp[(r,c)]=paths
            return paths
        
        return backtrack(0,0)
        