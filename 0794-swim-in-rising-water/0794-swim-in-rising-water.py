class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        min_heap=[]
        heappush(min_heap,(grid[0][0],0,0))
        visit=set([(0,0)])
        while min_heap:
            h,r,c=heappop(min_heap)
            if (r,c) == (rows-1,cols-1):
                return h
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visit:
                    heappush(min_heap,(max(h,grid[nr][nc]),nr,nc))
                    visit.add((nr,nc))
        