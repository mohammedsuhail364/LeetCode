class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # this question i m see the video of neetcode 
        # this one is similiar to what we done before topological sort but in different manner 
        # first ill explain this question it was simple enough like if we take a node as a root find its height and if it was minimum height compare to all nodes then add to result 
        # one key note is only two nodes existing in the result array why because we dont have three nodes as a same height that time we can take middle node this is also like a median concept
        # simply make a adjacency list 
        if not edges:
            return [0]
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        edges_count={} # similiar to incoming edges 
        leaves =deque()
        for src, nei in adj.items():
            # find the leaves and add to the queue why because we want to remove the leaves because that does not have minimum height only middle nodes does
            if len(nei)==1: # means leaf node has one parent like 
                leaves.append(src)
            edges_count[src]=len(nei)
        print(edges_count)
        while leaves:
            if n<=2:
                return list(leaves)
            for _ in range(len(leaves)):
                node=leaves.popleft()
                n-=1
                for nei in adj[node]:
                    edges_count[nei]-=1
                    if edges_count[nei]==1:
                        leaves.append(nei)
        
