class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dp=[[float('inf')]*(cols+1) for _ in range(rows+1)]
        dp[rows-1][cols-1]=grid[rows-1][cols-1] # base case
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if r==rows-1 and c==cols-1:
                    continue
                dp[r][c]=grid[r][c]+min(dp[r+1][c],dp[r][c+1])
        return dp[0][0]
        