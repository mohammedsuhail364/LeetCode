class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        # refer neetcode
        rows=len(grid)
        cols=len(grid[0])
        MOD=10**9+7
        dp=[[[0]*k for _ in range(cols+1)] for _ in range(rows+1)]
        target_remain = (k-(grid[rows-1][cols-1]%k))%k
        dp[rows-1][cols-1][target_remain]=1
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if r==rows-1 and c==cols-1:
                    continue
                for remain in range(k):
                    new_remain=(remain+grid[r][c])%k
                    dp[r][c][remain]=(
                        dp[r+1][c][new_remain]%MOD+
                        dp[r][c+1][new_remain]%MOD
                    )%MOD
        return dp[0][0][0]