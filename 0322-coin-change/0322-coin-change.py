class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount==0:
                return 0
            if amount<0:
                return float('inf')
            res=float('inf')
            for c in coins:
                res=min(res,1+dfs(amount-c))
            memo[amount]=res
            return res
        ans=dfs(amount)
        if ans==float('inf'):
            return -1
        return ans