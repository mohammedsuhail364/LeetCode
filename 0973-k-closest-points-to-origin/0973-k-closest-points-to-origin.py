class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for x,y in points:
            r=(x**2 + y**2)**0.5
            heappush(heap,(r,(x,y)))
        res=[]
        for x in range(k):
            r,(x,y)=heappop(heap)
            res.append([x,y])
        return res