class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        res=0
        temp=[[1]*cols for i in range(rows)]
        for i in range(rows):
            row_count=0
            for j in range(cols):
                if grid[i][j]:
                    row_count+=1
            if row_count>1:
                for j in range(cols):
                    if grid[i][j] and temp[i][j]:
                        res+=1
                        temp[i][j]=0
        j=0
        while j<cols:
            col_count=0
            for i in range(rows):
                if grid[i][j]:
                    col_count+=1
            if col_count>1:
                for i in range(rows):
                    if grid[i][j] and temp[i][j]: 
                        res+=1
                        temp[i][j]=0
            j+=1
        return res