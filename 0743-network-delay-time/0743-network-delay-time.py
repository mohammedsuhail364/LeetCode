class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        minHeap=[]
        heappush(minHeap,(0,k)) # (weight,node)
        dist={}
        while minHeap:
            w,v = heappop(minHeap)
            if v in dist:
                continue # already we store the time how much we spend for this node which is always minimum because of minHeap
            dist[v]=w
            for v1,w1 in adj[v]:
                if v1 not in dist:
                    heappush(minHeap,(w1+w,v1))
        return max(dist.values()) if len(dist)==n else -1