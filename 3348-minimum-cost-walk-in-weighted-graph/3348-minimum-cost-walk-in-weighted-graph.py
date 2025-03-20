import queue
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph={i:{} for i in range(n)}
        for u,v,w in edges:
            if v in graph[u]:
                graph[u][v]=graph[u][v]&w
                graph[v][u]=graph[v][u]&w
            else:
                graph[u][v]=w
                graph[v][u]=w
        def helper(node):
            q=queue.Queue()
            q.put(node)
            ans=-1
            while not q.empty():
                cur=q.get()
                parent[cur]=node
                if visited[cur]:
                    continue
                visited[cur]=True
                for nxt in graph[cur]:
                    if visited[nxt]:
                        continue
                    if ans==-1:
                        ans=graph[cur][nxt]
                    else:
                        ans=ans&graph[cur][nxt]
                    q.put(nxt)
            return ans
        parent=[i for i in range(n)]
        ans=[-1]*n
        visited=[False]*n
        res=[]
        for i in parent:
            if not visited[i]:
                ans[i]=helper(i)
        for src,dst in query:
            if parent[src]==parent[dst]:
                res.append(ans[parent[src]])
            else:
                res.append(-1)
        return res