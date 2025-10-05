class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(source,ocean):
            q=deque(source)
            while q:
                r,c=q.popleft()
                ocean[r][c]=True
                for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if 0<=nr<rows and 0<=nc<cols and not ocean[nr][nc] and heights[r][c]<=heights[nr][nc]: #this is the trick we dont check every time this ensure where is the main source comes 
                        q.append((nr,nc))
        rows=len(heights)
        cols=len(heights[0])
        pacific=[]
        atlantic=[]
        pac=[[False]*cols for _ in range(rows)]
        atl=[[False]*cols for _ in range(rows)]
        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((rows-1,c))
        for r in range(rows):
            pacific.append((r,0))
            atlantic.append((r,cols-1))
        bfs(pacific,pac)
        bfs(atlantic,atl)
        res=[]
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])
        return res
        