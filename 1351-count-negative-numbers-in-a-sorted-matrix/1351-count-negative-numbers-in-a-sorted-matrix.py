class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]<0:
                    res+=1
        return res