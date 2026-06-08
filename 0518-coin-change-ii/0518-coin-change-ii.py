class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache={}
        def dfs(i,cur):
            if (i,cur) in cache:
                return cache[i,cur]
            if i>=len(coins) or cur>amount:
                return 0
            if cur==amount:
                return 1
            skip=dfs(i+1,cur)
            include=dfs(i,cur+coins[i])
            cache[i,cur]=skip+include
            return cache[i,cur]

        return dfs(0,0)
        