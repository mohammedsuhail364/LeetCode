class Solution:
    def coloredCells(self, n: int) -> int:
        """
        Another pattern is 1+4+8+12+....
        
        """
        res=1
        for i in range(n):
            res+=(4*i)
        return res