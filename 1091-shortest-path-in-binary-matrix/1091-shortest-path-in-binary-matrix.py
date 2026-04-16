class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        q=deque([(0,0,0)])
        visited=set([(0,0)])
        ROWS=len(grid)
        COLS=len(grid[0])
        while q:
            r,c,d=q.popleft()
            if (r,c)==(ROWS-1,COLS-1):
                return d+1
            directions=[(r+1,c),(r-1,c),(r,c-1),(r,c+1),(r-1,c-1),(r+1,c+1),(r-1,c+1),(r+1,c-1)]
            for nr,nc in directions:
                if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==0 and (nr,nc) not in visited:
                    q.append((nr,nc,d+1))
                    visited.add((nr,nc))
        return -1
