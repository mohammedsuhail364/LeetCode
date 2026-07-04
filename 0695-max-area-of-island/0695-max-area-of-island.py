class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(row,col):
            q=deque([(row,col)])
            visit.add((row,col))
            l=0
            while q:
                r,c=q.popleft()
                l+=1
                for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visit and grid[nr][nc]:
                        q.append((nr,nc))
                        visit.add((nr,nc))
            return l
        ROWS=len(grid)
        COLS=len(grid[0])
        res=0
        visit=set()
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visit or grid[r][c]==0:
                    continue
                res=max(res,bfs(r,c))
        return res
