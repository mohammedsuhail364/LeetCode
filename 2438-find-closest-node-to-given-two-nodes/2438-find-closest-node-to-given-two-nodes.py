from collections import defaultdict,deque
class Solution:
    def closestMeetingNode(self, edges, node1: int, node2: int) -> int:
        n=len(edges)
        adj=defaultdict(list)
        def bfs(start):
            sh_dst=[-1]*n
            q=deque()
            q.append((start,0))
            visit=set([(start)])
            while q:
                for i in range(len(q)):
                    node,dst=q.popleft()
                    sh_dst[node]=dst
                    for child in adj[node]:
                        if child not in visit:
                            q.append((child,dst+1))
                            visit.add(child)

            return sh_dst

        for i in range(n):
            if edges[i]!=-1:
                adj[i].append(edges[i])
        print(adj)
        shortest_dist_node1=bfs(node1)
        shortest_dist_node2=bfs(node2)
        print(shortest_dist_node1)
        print(shortest_dist_node2)
        res=float('inf')
        di=defaultdict(list)
        for i in range(n):
            if shortest_dist_node1[i]!=-1 and shortest_dist_node2[i]!=-1:
                tmp=max(shortest_dist_node1[i],shortest_dist_node2[i])
                di[tmp].append(i)
        val=min(di) if di else -1 
        return min(di[val]) if val !=-1 else -1