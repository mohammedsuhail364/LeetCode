class Solution:
    def minTimeToReach(self, moveTime) -> int:
        rows=len(moveTime)
        cols=len(moveTime[0])
        heap=[(0,0,0)]
        dist=[[float('inf')]*cols for _ in range(rows) ]
        dist[0][0]=0
        while heap:
            currentTime,r,c=heapq.heappop(heap)
            if (r,c)==(rows-1,cols-1):
                return currentTime
            
            for nr,nc in [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]:
                if 0<=nr<rows and 0<=nc<cols:
                    waitTime=max(moveTime[nr][nc]-currentTime,0)
                    newArrivalTime=currentTime+1+waitTime
                    if newArrivalTime<dist[nr][nc]:
                        dist[nr][nc]=newArrivalTime
                        heapq.heappush(heap,(newArrivalTime,nr,nc))
        return -1
        


