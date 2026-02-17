class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        visit=[[False]*COLS for r in range(ROWS)]
        self.res=0
        def dfs(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLS:
                return
            if grid[r][c]=='0' or visit[r][c]:
                return
            visit[r][c]=True
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=='1' and not visit[r][c]:
                    self.res+=1
                    dfs(r,c)
        return self.res