class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap=[]
        for i in arr:
            heappush(min_heap,(abs(i-x),i))
        res=[]
        while k:
            diff,val=heappop(min_heap)
            res.append(val)
            k-=1
        return sorted(res)