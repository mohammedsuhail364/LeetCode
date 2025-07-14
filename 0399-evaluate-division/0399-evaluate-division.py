class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # refer neetcode
        adj=defaultdict(list)
        for i,eq in enumerate(equations):
            a,b=eq
            adj[a].append((b,values[i]))
            adj[b].append((a,1/values[i]))
        def bfs(src,target):
            if src not in adj or target not in adj:
                return -1
            if src==target:
                return 1
            q=deque([(src,1)])
            visit=set([(src)])
            while q:
                n,w=q.popleft()
                if n==target:
                    return w
                for nei,wei in adj[n]:
                    if nei not in visit:
                        q.append((nei,w*wei))
                        visit.add(nei)
            return -1
        return [bfs(i,j) for i,j in queries]