class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        n=len(cost)
        res=0
        for i in range(1,n+1): 
            if i%3==0:
                continue
            res+=cost[i-1]
        return res