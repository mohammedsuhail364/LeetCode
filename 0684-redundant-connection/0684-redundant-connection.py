class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node,parent,visit):
            if node in visit:
                return True
            visit.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei,node,visit):
                    return True
            return False
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit=set()
            if dfs(u,-1,visit):
                return [u,v]
        