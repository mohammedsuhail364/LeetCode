class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        rows=len(grid)
        cols=len(grid[0])
        MOD=10**9+7
        dp=[[[-1]*k for _ in range(cols)] for _ in range(rows)]
        def dfs(r,c,cur_sum):
            if r==rows-1 and c==cols-1:
                if (cur_sum+grid[r][c])%k==0:
                    return 1
                return 0
            if r>=rows or r<0 or c>=cols or c<0:
                return 0
            if dp[r][c][cur_sum] != -1:
                return dp[r][c][cur_sum]
            count=(
                dfs(r+1,c,(cur_sum+grid[r][c])%k)+
                dfs(r,c+1,(cur_sum+grid[r][c])%k)
                )
            dp[r][c][cur_sum]= count%MOD
            return dp[r][c][cur_sum]
        return dfs(0,0,0)