class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod=10**9+7
        @lru_cache(None)
        def dfs(val,prev):
            if val >n:
                return 0
            if val==n:
                return 1 
            if ((prev+1)**x)>n-val:
                return 0
            # skip the current one
            ways =( dfs(val,prev+1))%mod
            # include the current one
            ways +=(dfs(val+((prev+1)**x),prev+1))%mod
            return ways
        return dfs(0,0)%mod
         