class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        row=set()
        col=set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    row.add(r)
                    col.add(c)
        return (max(row) - min(row)+1) * (max(col)-min(col)+1)