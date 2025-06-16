class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        q=deque()
        time=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c,0))
        while q and fresh>0:
            r,c,t=q.popleft()
            for nr,nc in [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]:
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    grid[nr][nc] = 2
                    q.append((nr,nc,t+1))
                    fresh-=1
                    time=t+1
        return time if fresh==0 else -1

