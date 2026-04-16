class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # this question is based on the multi source bfs
        # start with the all rotten oranges and find the minimum time
        # refer neetcode
        q=deque()
        ROWS=len(grid)
        COLS=len(grid[0])
        fresh=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r,c,0)) 
                elif grid[r][c]==1:
                    fresh+=1
        time=0
        while q and fresh:
            r,c,t=q.popleft()
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    q.append((nr,nc,t+1))
                    fresh-=1
                    time=t+1
        return time if fresh==0 else -1