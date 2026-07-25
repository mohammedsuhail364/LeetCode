from typing import List
from collections import Counter
from heapq import heappop,heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap=[]
        c=Counter(nums)
        for key,val in c.items():
            heappush(minHeap,(val,key))
            if len(minHeap)>k:
                heappop(minHeap)
        res=[]
        for val,key in minHeap:
            res.append(key)
        return res