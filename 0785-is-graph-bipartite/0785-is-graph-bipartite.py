class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # this question is putting different colors to the neighbours 
        # in the union find way of thinking like grouping neighbours without the node 
        # group neighbours but the current node not in that group
        # same template with some adjustments
        parent=list(range(len(graph)+1))
        rank=[1]*(len(graph)+1)
        n=len(graph)
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]] # path compression
                x=parent[x]
            return x

        def union(x,y):
            px,py=find(x),find(y)
            if px==py:return
            if rank[px]>rank[py]:
                px,py=py,px
            parent[py]=px
            rank[px]+=rank[py]

        for u in range(n):
            if not graph[u]:
                continue
            for v in graph[u]:
                if find(u)==find(graph[u][0]):
                    return False
                # group their neigbours
                union(v,graph[u][0])
        return True