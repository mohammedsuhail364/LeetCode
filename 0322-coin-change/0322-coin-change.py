class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[inf]*(amount+1)
        dp[amount]=0
        for cur in range(amount,-1,-1):
            for c in coins:
                dp[cur]=min(dp[cur],1+(dp[cur+c] if cur+c<=amount else inf))
        return -1 if dp[0]==inf else dp[0]
        # cache={}
        # def dfs(cur):
        #     if cur in cache:
        #         return cache[cur]
        #     if cur>amount:
        #         return inf
        #     if cur==amount:
        #         return 0
        #     cache[cur]=inf
        #     for c in coins:
        #         cache[cur]=min(cache[cur],1+dfs(cur+c))
        #     return cache[cur]
        # res = dfs(0)
        # if res==inf:
        #     return -1
        # return res