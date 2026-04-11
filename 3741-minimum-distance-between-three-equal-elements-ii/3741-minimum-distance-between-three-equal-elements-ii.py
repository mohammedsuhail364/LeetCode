class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # store the values based on index
        indices=defaultdict(list)
        res=inf
        for i,v in enumerate(nums):
            indices[v].append(i)
        for idx in indices.values():
            if len(idx)<3 : # not valid to find minimum
                continue
            for i in range(len(idx)-2):
                val=abs(idx[i+1]-idx[i])+abs(idx[i+2]-idx[i+1])+abs(idx[i+2]-idx[i])
                res=min(res,val)
        return res if res!=inf else -1