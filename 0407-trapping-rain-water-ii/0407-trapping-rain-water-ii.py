class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # if you dont understand go and debug this 
        min_heap=[]
        rows=len(heightMap)
        cols=len(heightMap[0])
        for r in range(rows):
            for c in range(cols):
                if r in [0,rows-1] or c in [0,cols-1]:
                    heapq.heappush(min_heap,(heightMap[r][c],r,c))
                    heightMap[r][c]=-1
        res=0
        max_hei=-1
        while min_heap:
            h,r,c=heapq.heappop(min_heap)
            max_hei=max(max_hei,h)
            res+=max_hei-h
            neighbours=[(r,c+1),(r,c-1),(r+1,c),(r-1,c)]
            for nr,nc in neighbours:
                if (nr<0 or nc<0 or nr==rows or nc==cols or heightMap[nr][nc]==-1):
                    continue
                heapq.heappush(min_heap,(heightMap[nr][nc],nr,nc))
                heightMap[nr][nc]=-1
        return res