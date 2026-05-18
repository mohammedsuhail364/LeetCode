class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        def bfs(row,col):
            min_heap=[(grid[row][col],row,col)]
            visit=set()
            visit.add((row,col))
            cur=0
            while min_heap:
                cost,r,c=heappop(min_heap)
                if (r,c)==(ROWS-1,COLS-1):
                    return cost
                for nr,nc in [(r+1,c),(r,c+1)]:
                    if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visit:
                        heappush(min_heap,(grid[nr][nc]+cost,nr,nc))
                        visit.add((nr,nc))

        return bfs(0,0)

