class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        min_heap=[(grid[0][0],0,0)] # time,row,col
        visit=set()
        visit.add((0,0))
        res=0
        while min_heap:
            time,r,c=heappop(min_heap)
            if (r,c)==(rows-1,cols-1):
                return max(res,grid[r][c])
            res=max(res,time)
            directions=[(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
            for nr,nc in directions:
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visit:
                    heappush(min_heap,(grid[nr][nc],nr,nc))
                    visit.add((nr,nc))
        