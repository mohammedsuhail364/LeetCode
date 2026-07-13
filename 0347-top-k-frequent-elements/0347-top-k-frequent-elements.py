class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        for i,j in Counter(nums).items():
            heappush(heap,(j,i))
            if len(heap)>k:
                heappop(heap)
        res=[]
        for _,key in heap:
            res.append(key)
        return res