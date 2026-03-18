class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        pre_sum=[[0]*(COLS+1) for _ in range(ROWS+1)]
        for r in range(ROWS):
            prefix=0
            for c in range(COLS):
                prefix+=grid[r][c]
                above=pre_sum[r][c+1]
                pre_sum[r+1][c+1]=prefix+above

        res=0
        for r in range(ROWS+1):
            for c in range(COLS+1):
                if r==0 or c==0:
                    continue
                if pre_sum[r][c]<=k:
                    res+=1
                else:
                    break
        return res