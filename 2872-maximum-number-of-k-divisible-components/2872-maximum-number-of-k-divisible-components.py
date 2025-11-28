class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # refer neetcode
        adj=defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        res=0
        def dfs(cur,parent):
            total=values[cur]
            for child in adj[cur]:
                if child==parent:
                    continue
                total+=dfs(child,cur)
            if total%k==0:
                nonlocal res
                res+=1
                return 0 # imagine cut the current one

            return total
        dfs(0,-1) # start from any node 
        return res