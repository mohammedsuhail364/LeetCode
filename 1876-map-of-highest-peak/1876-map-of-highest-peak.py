class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows=len(isWater)
        cols=len(isWater[0])
        q=deque([])
        visit=set()
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c]:
                    isWater[r][c]=0
                    q.append((r,c))
                    visit.add((r,c))
        while q:
            r,c=q.popleft()
            for nr,nc in [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]:
                if (nr<0 or nc<0 or nr==rows or nc==cols or (nr,nc) in visit):
                    continue
                isWater[nr][nc]=isWater[r][c]+1
                q.append((nr,nc))
                visit.add((nr,nc))
        return isWater
        
        