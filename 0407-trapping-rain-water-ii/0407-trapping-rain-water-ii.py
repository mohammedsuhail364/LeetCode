class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        min_heap=[]
        rows=len(heightMap)
        cols=len(heightMap[0])
        # add borders in heap
        for r in range(rows):
            for c in range(cols):
                if r in (0,rows-1) or c in (0,cols-1):
                    heappush(min_heap,(heightMap[r][c],r,c))
                    heightMap[r][c]=-1
        # start the multisource bfs
        res=0
        max_height=-1
        while min_heap:
            h,r,c=heappop(min_heap)
            max_height=max(max_height,h)
            res+=(max_height-h)
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=nr<rows and 0<=nc<cols and heightMap[nr][nc]!=-1:
                    heappush(min_heap,(heightMap[nr][nc],nr,nc))
                    heightMap[nr][nc]=-1
        return res