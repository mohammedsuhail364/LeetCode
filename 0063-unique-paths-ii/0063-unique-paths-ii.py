class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return 0
        self.res=0
        rows=len(grid)
        cols=len(grid[0])
        def backtrack(r,c):
            if (r,c)==(rows-1,cols-1):
                self.res+=1
                return
            temp=grid[r][c]
            grid[r][c]=-1
            for nr,nc in [(r+1,c),(r,c+1)]:
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==0:
                    backtrack(nr,nc)
            grid[r][c]=temp
        backtrack(0,0)

        return self.res
        