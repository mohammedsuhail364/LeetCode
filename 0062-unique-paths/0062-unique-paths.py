class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)]
        dp[m-1][n-1]=1 # base case
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if r==m-1 and c==n-1:
                    continue
                down=dp[r+1][c] if r+1<m else 0
                right=dp[r][c+1] if c+1<n else 0
                dp[r][c]=down+right
        return dp[0][0]
