from collections import defaultdict,deque
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        min_heap=[(0,k)]
        dist={}
        while min_heap:
            time,node=heappop(min_heap)
            if node in dist:
                continue
            dist[node]=time
            for nei,wei in adj[node]:
                if nei not in dist:
                    heappush(min_heap,(time+wei,nei))
        return max(dist.values()) if len(dist)==n else -1