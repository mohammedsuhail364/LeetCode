class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows=len(grid)
        cols=len(grid[0])
        def bfs(row,col,k):
            q=deque([(row,col,0,k)])
            visit=set([(row,col,k)])
            while q:
                for i in range(len(q)):
                    r,c,val,k_val=q.popleft()
                    if (r,c)==(rows-1,cols-1):
                        return val
                    for nr,nc in [(r,c-1),(r,c+1),(r-1,c),(r+1,c)]:
                        if 0<=nr<rows and 0<=nc<cols:
                            nk=k_val-grid[nr][nc]
                            if nk>=0 and (nr,nc,nk) not in visit:
                                q.append((nr,nc,val+1,nk))
                                visit.add((nr,nc,nk))
                            
            return -1
        return bfs(0,0,k)
            
