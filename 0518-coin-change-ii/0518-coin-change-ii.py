class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        def dfs(i,cur_sum):
            if (i,cur_sum) in memo:
                return memo[(i,cur_sum)]
            if cur_sum==amount:
                return 1
            if i>=len(coins) or cur_sum>amount:
                return 0
            skip=dfs(i+1,cur_sum)
            include=dfs(i,cur_sum+coins[i])
            memo[(i,cur_sum)]= skip+include
            return memo[(i,cur_sum)]
        return dfs(0,0)