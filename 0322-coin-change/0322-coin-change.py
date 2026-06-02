class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache={}
        def dfs(rem):
            if rem in cache:
                return cache[rem]
            if rem==0:
                return 0
            if rem<0:
                return inf
            cache[rem]=inf
            for c in coins:
                cache[rem]=min(cache[rem],1+dfs(rem-c))
            return cache[rem]
            
        res= dfs(amount)
        if res!=inf:
            return res
        return -1