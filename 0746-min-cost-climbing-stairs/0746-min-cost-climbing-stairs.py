class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache={}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i>=len(cost):
                return 0
            one_step=cost[i]+dfs(i+1)
            two_step=cost[i]+dfs(i+2)
            cache[i] = min(one_step,two_step)
            return cache[i]
        return min(dfs(0),dfs(1))