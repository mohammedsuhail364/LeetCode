class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        minHeap=[]
        cur=0
        for pas,s,e in trips:
            while minHeap and minHeap[0][0]<=s:
                end,p = heappop(minHeap)
                cur-=p
            cur+=pas
            heappush(minHeap,(e,pas))
            if cur>capacity:
                return False
        return True
        
                    