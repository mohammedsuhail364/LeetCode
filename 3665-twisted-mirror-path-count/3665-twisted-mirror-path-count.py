class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        # we need a previous direction
        ROWS = len(grid)
        COLS = len(grid[0])
        MOD = 10**9+7 
        @lru_cache(None)
        def dfs(r,c,dire):
            if (r,c)==(ROWS-1,COLS-1):return 1
            if r<0 or r>=ROWS or c<0 or c>=COLS:
                return 0
            res=0
            if not dire or grid[r][c]==0:
                res+=(dfs(r,c+1,"right")%MOD)
                res+=(dfs(r+1,c,"down")%MOD)
            else:
                if dire=="right":
                    res+=(dfs(r+1,c,"down")%MOD)
                elif dire=="down":
                    res+=(dfs(r,c+1,"right")%MOD)
            return res%MOD
        return dfs(0,0,None)%MOD

