class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows=len(grid)
        cols=len(grid[0])
        di=defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                di[r-c].append(grid[r][c])
        for i in di:
            if i>=0:
                di[i].sort()
            else:
                di[i].sort(reverse=True)
        for r in range(rows):
            for c in range(cols):
                grid[r][c]=di[r-c].pop()
        return grid