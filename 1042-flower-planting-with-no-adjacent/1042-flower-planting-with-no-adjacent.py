class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # this question is much more simpler because we can find the color of the current node expect neighbours color , answer is possible that is the main advantage of this question 
        res=[0]*(n+1)
        adj=defaultdict(list)
        for u,v in paths:
            adj[u].append(v)
            adj[v].append(u)
        for u in range(1,n+1):
            used={res[nei] for nei in adj[u]}
            for color in range(1,5):
                if color not in used:
                    res[u]=color
                    break
        return res[1:]