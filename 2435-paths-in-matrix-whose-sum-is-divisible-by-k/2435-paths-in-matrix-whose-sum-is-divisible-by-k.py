class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        rows=len(grid)
        cols=len(grid[0])
        MOD=10**9+7
        memo={}
        def dfs(r,c,cur_sum):
            if(r,c,cur_sum) in memo:
                return memo[(r,c,cur_sum)]
            if r==rows-1 and c==cols-1:
                if (cur_sum+grid[r][c])%k==0:
                    return 1
                return 0
            if r>=rows or c>=cols:
                return 0
            new_sum=(cur_sum+grid[r][c])%k
            down=dfs(r+1,c,new_sum)
            right=dfs(r,c+1,new_sum)
            final=(down+right)%MOD
            memo[(r,c,cur_sum)]=final%MOD
            return final%MOD
        return dfs(0,0,0)
