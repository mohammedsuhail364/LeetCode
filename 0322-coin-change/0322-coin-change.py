class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def dfs(cur_sum):
            if cur_sum in memo:
                return memo[cur_sum]
            if cur_sum==amount:
                return 0
            if cur_sum>amount:
                return float('inf')
            res=float('inf')
            for c in coins:
                res=min(res,1+dfs(cur_sum+c))
            memo[cur_sum]=res
            return res
        ans=dfs(0)
        if ans==float('inf'):
            return -1
        return ans