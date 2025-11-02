class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def helper(r,c):
            for i in range(r+1,m):
                if grid[i][c] in [1,2]:
                    break
                grid[i][c]=3
            for i in range(c+1,n):
                if grid[r][i] in [1,2]:
                    break
                grid[r][i]=3
            for i in range(r-1,-1,-1):
                if grid[i][c] in [1,2]:
                    break
                grid[i][c]=3
            for i in range(c-1,-1,-1):
                if grid[r][i] in [1,2]:
                    break
                grid[r][i]=3
            
        grid=[[0]*n for _ in range(m)]
        # 0->notguarded 1->guards 2->walls 3->guarded
        for r,c in guards:
            grid[r][c]=1
        for r,c in walls:
            grid[r][c]=2
        for r,c in guards:
            helper(r,c)
        res=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    res+=1
        return res
