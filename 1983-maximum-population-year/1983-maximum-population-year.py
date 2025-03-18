class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        res=[0]*101
        for b,d in logs:
            for x in range(b,d):
                res[x-1950]+=1
        max_val=max(res)
        return 1950+res.index(max_val)