class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        min_heap=[(grid[0][0],0,0)] # (r,c,t)
        visit=set([(0,0)])
        while min_heap:
            h,r,c=heappop(min_heap)
            if (r,c)==(ROWS-1,COLS-1):
                return h
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visit:
                    height=max(h,grid[nr][nc])
                    heappush(min_heap,(height,nr,nc))
                    visit.add((nr,nc))
        