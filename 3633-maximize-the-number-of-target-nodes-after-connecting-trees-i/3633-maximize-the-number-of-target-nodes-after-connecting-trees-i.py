class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def bfs(start,adj,n):
            
            q=deque([(start,-1)])
            count=0
            while q and n>=0:
                count+=len(q)
                for i in range(len(q)):
                    u,parent=q.popleft()
                    for v in adj[u]:
                        if v!=parent:
                            q.append((v,u))
                n-=1
            return count
        n=len(edges1)+1
        m=len(edges2)+1
        adj1=defaultdict(list)
        adj2=defaultdict(list)
        for u,v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u,v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
        best=0
        for i in range(m):
            connections=bfs(i,adj2,k-1)
            best=max(connections,best)
        res=[]
        for i in range(n):
            connections=bfs(i,adj1,k)
            res.append(connections+best)
        return res
        