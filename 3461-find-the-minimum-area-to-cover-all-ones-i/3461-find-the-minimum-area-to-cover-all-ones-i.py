class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        min_row=rows
        max_row=0
        min_col=cols
        max_col=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    min_row=min(min_row,r)
                    max_row=max(max_row,r)
                    min_col=min(min_col,c)
                    max_col=max(max_col,c)
        return (max_row-min_row+1)*(max_col-min_col+1)