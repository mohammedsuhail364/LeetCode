class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        The Core Intuition
        In an undirected graph, an edge (u, v) is a bridge (critical connection) if there is no other path from u to v besides that direct edge.
        So the question becomes: how do we know if an edge has an alternate path?
        Key insight: During DFS, when you visit nodes, you assign them a discovery time (the order you visited them). If from node v (or any node reachable from v), you can reach back to an ancestor of u using a back-edge, then the edge (u → v) is NOT a bridge — because there's a cycle covering it.

        Two Arrays Tarjan Uses
        disc[node] — Discovery time. When did DFS first visit this node?
        low[node] — The lowest discovery time reachable from the subtree rooted at this node (using back-edges to ancestors).
        Think of low[node] as: "how far back can I reach using alternate paths?"

        The Bridge Condition
        After fully exploring node v (child of u):
        if low[v] > disc[u]  →  edge (u, v) is a BRIDGE
        Why? If low[v] > disc[u], it means node v (and everything below it) cannot reach back to u or any ancestor of u. So removing edge (u → v) disconnects v's subtree entirely.
        """
        # refer take u forward
        adj=defaultdict(list)
        res=[]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        res=[]
        # discovery time of this node
        disc=[-1]*n # visit also 
        # lowest discovery of this node
        low=[-1]*n
        timer=0
        def dfs(node,parent):
            nonlocal timer
            disc[node]=low[node]=timer
            timer+=1
            for nei in adj[node]:
                if nei==parent:
                    continue
                if disc[nei]==-1: # not visited node
                    dfs(nei,node)
                    low[node]=min(low[node],low[nei])
                    # check it was critical connection
                    if low[nei]>disc[node]:
                        res.append([node,nei])
                else: # already visited but we can come from this node also known as back edge
                    low[node]=min(low[node],disc[nei])

        dfs(0,-1)
        return res