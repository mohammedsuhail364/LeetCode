from collections import deque
class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        def bfs(row,col):
            total = grid[row][col]
            q=deque()
            q.append((row,col))
            grid[row][col] = 0
            while q:
                r,c = q.popleft()
                for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]!=0:
                        total+=grid[nr][nc]
                        grid[nr][nc] =0
                        q.append((nr,nc)) 

            return total
        ROWS,COLS = len(grid),len(grid[0])
        visit = set()
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]!=0:
                    total = bfs(r,c)
                    if total%k==0:res+=1
        return res