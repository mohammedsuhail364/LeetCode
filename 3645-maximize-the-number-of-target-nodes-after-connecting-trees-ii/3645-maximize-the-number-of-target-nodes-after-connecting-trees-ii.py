class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # refer tech dose
        n=len(edges1)+1
        m=len(edges2)+1
        def bfs(start,adj,included=None):
            visited=set()
            q=deque([(start,-1)])
            count=0
            k=0
            while q:
                size=len(q)
                count+=size if k%2==0 else 0
                for _ in range(size):
                    u,parent=q.popleft()
                    if included and k%2==0:
                        included[u]=True
                    for v in adj[u]:
                        if v!=parent:
                            q.append((v,u))
                k+=1
            return count
        adj1=defaultdict(list)
        adj2=defaultdict(list)
        for u,v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u,v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
        best=0
        
        tree2_even_count=bfs(0,adj2)
        tree2_odd_count=m-tree2_even_count
        best=max(tree2_even_count,tree2_odd_count)
        included=[False] * n  
        tree1_even_count=bfs(0,adj1,included)
        tree1_odd_count=n-tree1_even_count
        res=[0]*n
        for i in range(n):
            if included[i]:
                res[i]=tree1_even_count+best
            else:
                res[i]=tree1_odd_count+best
        return res