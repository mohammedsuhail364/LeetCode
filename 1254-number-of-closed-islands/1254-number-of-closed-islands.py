class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        def bfs(row,col):
            q=deque()
            q.append((row,col))
            grid[row][col] = 2
            while q:
                r,c = q.popleft()
                for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==0:
                        grid[nr][nc]=2
                        q.append((nr,nc)) 
        ROWS = len(grid)
        COLS = len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if (r==ROWS-1 or r==0 or c==0 or c==COLS-1) and grid[r][c]==0:
                    bfs(r,c)
        res=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    res+=1
                    bfs(r,c)
        
        return res
        