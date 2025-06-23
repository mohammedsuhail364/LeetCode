class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node,parent,visit):
            if node in visit:
                return True
            visit.add(node)
            for nei in adj[node]:
                if nei==parent:
                    continue
                if dfs(nei,node,visit):
                    return True
            return False
        adj=defaultdict(list)
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
            visit=set()
            if dfs(src,-1,visit):
                return [src,dst]
        return []