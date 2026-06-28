class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # refer this https://www.youtube.com/watch?v=iQBxxTZDajU
        n=len(graph)
        q=deque([(1<<i,i,0) for i in range(n)]) #(mask,node,dist)
        # this question basically a normal BFS with some bit mask in the deque we can all the index in below n
        # mask indicates for eg: i=1 means we can fill the 1 (000010) like this 
        visited=set([(1<<i,i) for i in range(n)])
        while q:
            mask,node,dist=q.popleft()
            if mask==(1<<n) -1 : # (1<<n) -1  refers all one's like this (1111111)
                return dist
            for nei in graph[node]:
                new_mask=mask|(1<<nei)
                if (new_mask,nei) not in visited:
                    visited.add((new_mask,nei))
                    q.append((new_mask,nei,dist+1))
        