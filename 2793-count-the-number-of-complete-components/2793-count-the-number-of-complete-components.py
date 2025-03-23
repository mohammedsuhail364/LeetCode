from collections import defaultdict,deque

class Solution:
    def countCompleteComponents(self, n: int, edges) -> int:
        count=0
        visited=set()
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def bfs(i):
            q=deque([(i)])
            visited.add(i)
            nodes={i}
            edge_count=0
            while q:
                node=q.popleft()
                for nxt in adj[node]:
                    edge_count+=1
                    if nxt in visited:
                        continue
                    q.append(nxt)
                    visited.add(nxt)
                    nodes.add(nxt)
            size=len(nodes)
            edges=(size*(size-1))//2
            
            return edges==(edge_count//2)

        for i in range(n):
            if i in visited:
                continue
            if bfs(i):
                count+=1
        return count