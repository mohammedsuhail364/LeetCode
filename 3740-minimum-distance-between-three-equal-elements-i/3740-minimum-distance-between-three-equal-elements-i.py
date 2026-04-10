class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices=defaultdict(list) # seperate by index
        for i,v in enumerate(nums):
            indices[v].append(i)
        res=inf
        for idx in indices.values():
            if len(idx)<3:
                continue # no result found 
            n=len(idx)
            for i in range(n-2): # check the other two 
                dist=abs(idx[i+1]-idx[i])+abs(idx[i+2]-idx[i+1])+abs(idx[i+2]-idx[i])
                res=min(res,dist)
            
        return res if res!=inf else -1