class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(list)
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        q=deque([(1)]) #(starting node,weight) 
        visit=set([(1)])
        res=inf
        while q:
            node=q.popleft()
            for nei,wei in adj[node]:
                if nei not in visit:
                    q.append((nei))
                    visit.add(nei)
                res=min(res,wei)
        return res