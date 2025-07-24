class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n=len(nums)
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        subtree_xor=[0]*n
        descendants=[set() for i in range(n) ]
        def dfs(node,parent):
            subtree_xor[node]=nums[node]
            descendants[node].add(node)
            for nei in adj[node]:
                if nei != parent:
                    dfs(nei,node)
                    subtree_xor[node] ^= subtree_xor[nei]
                    descendants[node].update(descendants[nei])
        dfs(0,-1)
        total_xor=subtree_xor[0]
        min_score=inf
        for i in range(1,n):
            for j in range(i+1,n):
                xor_i=subtree_xor[i]
                xor_j=subtree_xor[j]
                if j in descendants[i]:
                    com1=xor_j
                    com2=xor_i ^ xor_j
                    com3=total_xor ^ xor_i
                elif i in descendants[j]:
                    com1=xor_i
                    com2=xor_j ^ xor_i
                    com3=total_xor ^ xor_j
                else:
                    com1=xor_i
                    com2=xor_j 
                    com3=total_xor ^ xor_i ^ xor_j
                score = max(com1,com2,com3) - min(com1,com2,com3)
                min_score=min(min_score,score)
        return min_score
