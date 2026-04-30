class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        parent=[i for i in range(n+1)]
        rank=[1]*(n+1)
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x

        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return False # cycle detected 
            if rank[py]>rank[px]:
                px,py=py,px
            parent[py]=px
            rank[px]+=rank[py]
            return True
        # this question is similiar to bipartite 
        # we can group the neighbours as like the bipartite question 
        # start with making adj list 
        adj=defaultdict(list)
        for u,v in dislikes:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        for u in range(1,n+1):
            for v in adj[u]:
                if find(u)==find(adj[u][0]):
                    return False
                union(v,adj[u][0])
        return True
