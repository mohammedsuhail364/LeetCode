from heapq import heappush,heappop,heapify
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[-s for s in stones]
        heapify(max_heap)
        while len(max_heap)>1:
            x=-heappop(max_heap)
            y=-heappop(max_heap)
            if x!=y:
                heappush(max_heap,-(x-y))
        return 0 if len(max_heap)==0 else -max_heap[0]