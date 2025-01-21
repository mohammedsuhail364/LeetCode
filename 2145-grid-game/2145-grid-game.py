class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        prefixRow1=grid[0].copy()
        prefixRow2=grid[1].copy()
        for i in range(1,n):
            prefixRow1[i]+=prefixRow1[i-1]
            prefixRow2[i]+=prefixRow2[i-1]
        res=float('inf')
        for i in range(n):
            top=prefixRow1[-1]-prefixRow1[i]
            bottom=prefixRow2[i-1] if i>0 else 0
            secondRobot=max(top,bottom)
            res=min(secondRobot,res)
        return res