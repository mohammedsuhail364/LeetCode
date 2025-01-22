class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows=len(isWater)
        cols=len(isWater[0])
        q=deque([])
        res=[[-1]*cols for i in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c]:
                    res[r][c]=0
                    q.append((r,c))
        while q:
            r,c=q.popleft()
            for nr,nc in [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]:
                if (nr<0 or nc<0 or nr==rows or nc==cols or res[nr][nc]!=-1):
                    continue
                res[nr][nc]=res[r][c]+1
                q.append((nr,nc))
                
        return res
        
        