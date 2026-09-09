class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # refer neetcode
        ROWS = len(heightMap)
        COLS =len(heightMap[0])
        # in this question we need to think slightely different like first add non water holding places and get the max val and with that max if we find some thing lower than this we can add in our res so we first add the corners which naturally cannot hold water and we process level by level at the time we use the minHeap
        minHeap=[]
        maxVal=0
        res=0
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0,ROWS-1] or c in [0,COLS-1]:
                    heappush(minHeap,(heightMap[r][c],r,c))
                    heightMap[r][c] = -1 # just for visited purpose
        # in this we get the lower non water holding elements and process if we get the element which is lower than this we can add res because apart from that surrounding defintely higher than that
        while minHeap:
            h,r,c = heappop(minHeap)
            maxVal=max(maxVal,h)
            res+=(maxVal-h)
            for nr,nc in [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]:
                if 0<=nr<ROWS and 0<=nc<COLS and heightMap[nr][nc]!=-1:
                    heappush(minHeap,(heightMap[nr][nc],nr,nc))
                    heightMap[nr][nc]=-1
        return res