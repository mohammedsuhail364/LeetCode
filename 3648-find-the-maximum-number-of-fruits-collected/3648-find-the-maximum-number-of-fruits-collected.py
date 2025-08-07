class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        # refer tech dose
        n=len(fruits)
        first=sum(fruits[i][i] for i in range(n))
        def make_dirs(dirs):
            @lru_cache(None)
            def dfs(r,c,moves):
                if (r,c)==(n-1,n-1):
                    return 0 if moves==0 else inf
                if moves == 0 or r==c:
                    return inf
                best=-1
                for dr,dc in dirs:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<n and 0<=nc<n:
                        val=dfs(nr,nc,moves-1)
                        if val != inf:
                            best=max(best,val)
                return inf if best<0 else fruits[r][c] + best
            return dfs
        # second 
        down_dirs=[(1,-1),(1,0),(1,1)]
        dfs_down=make_dirs(down_dirs)
        second=dfs_down(0,n-1,n-1)
        # third 
        up_dirs=[(-1,1),(0,1),(1,1)]
        dfs_up=make_dirs(up_dirs)
        third=dfs_up(n-1,0,n-1)
        return first+second+third
    