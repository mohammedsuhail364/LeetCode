class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        res=0
        row_count=[0]*rows
        col_count=[0]*cols
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    row_count[r]+=1
                    col_count[c]+=1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and max(row_count[r],col_count[c])>1 :
                    res+=1
        return res