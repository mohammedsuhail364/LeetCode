class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def build_adj(edges):
            adj=defaultdict(list)
            for i,j in edges:
                adj[i].append(j)
                adj[j].append(i)
            return adj
        adj1=build_adj(edges1)
        adj2=build_adj(edges2)
        def get_diameter(cur,par,adj):
            max_d=0
            max_leaf_path=[0,0]
            for nei in adj[cur]:
                if par==nei:
                    continue
                nei_d,nei_max_leaf_path=get_diameter(nei,cur,adj)
                max_d=max(max_d,nei_d)
                heappush(max_leaf_path,nei_max_leaf_path)
                heappop(max_leaf_path)
            max_d=max(max_d,sum(max_leaf_path))
            return [max_d,1+max(max_leaf_path)]
        d1,_=get_diameter(0,-1,adj1)
        d2,_=get_diameter(0,-1,adj2)

        return max(d1,d2,ceil(d1/2)+1+ceil(d2/2))