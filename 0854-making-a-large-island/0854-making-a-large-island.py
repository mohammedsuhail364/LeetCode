from collections import deque
class Solution:
    def largestIsland(self, grid) -> int:
        rows=len(grid)
        cols=len(grid[0])
        island_max={}
        unique_id=2 # start from 2 because of 0 , 1

        def bfs(r,c,id):
            q=deque([(r,c)])
            grid[r][c]=id
            size=1
            while q:
                row,col=q.popleft()
                for nr,nc in [(row,col+1),(row,col-1),(row+1,col),(row-1,col)]:
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] ==1:
                        grid[nr][nc]=id
                        size+=1
                        q.append((nr,nc))
            return size


        # step 1 -> to mark the islands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    island_max[unique_id]=bfs(r,c,unique_id)
                    unique_id+=1
        if not island_max:
            if grid[0][0]==1:
                return rows*cols
            else:
                return 1
        #  step 2 -> to mark the 0 into 1:
        max_island = max(island_max.values(), default=0)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    seen=set()
                    new_size=1
                    for nr,nc in [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]:
                        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] >1:
                            seen.add(grid[nr][nc])
                    for i in seen:
                        new_size+=island_max[i]
                    max_island=max(new_size,max_island)
        return max_island