class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache={}
        def dfs(cur):
            if cur in cache:
                return cache[cur]
            if cur>amount:
                return inf
            if cur==amount:
                return 0
            cache[cur]=inf
            for c in coins:
                cache[cur]=min(cache[cur],1+dfs(cur+c))
            return cache[cur]
        res = dfs(0)
        if res==inf:
            return -1
        return res