class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=defaultdict(list)
        for u,v in tickets:
            adj[u].append(v)
        for i,j in adj.items():
            j.sort(reverse=True)
        res=[]
        def dfs(node):
            while adj[node]:
                next_node=adj[node].pop()
                dfs(next_node)
            res.append(node)
        dfs("JFK")
        return res[::-1]
        