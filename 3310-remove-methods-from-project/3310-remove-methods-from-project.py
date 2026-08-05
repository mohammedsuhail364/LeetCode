class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for u,v in invocations:
            adj[u].append(v)
        visit=set() # visited by K
        def dfs(node):
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
        visit.add(k)
        dfs(k)
        for u,v in invocations:
            if u not in visit and v in visit:
                return list(range(n))
        return [i for i in range(n) if i not in visit]
        