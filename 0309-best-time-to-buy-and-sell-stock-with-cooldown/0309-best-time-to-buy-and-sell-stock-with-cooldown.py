class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # refer neetcode
        cache={}
        def dfs(i,buying):
            if i>=len(prices):
                return 0
            if (i,buying) in cache:
                return cache[(i,buying)]
            if buying:
                buy=dfs(i+1,not buying)-prices[i]
                cooldown=dfs(i+1,buying)
                cache[i,buying]=max(buy,cooldown)
            else:
                sell=dfs(i+2,not buying)+prices[i]
                cooldown=dfs(i+1,buying)
                cache[i,buying]=max(sell,cooldown)
            return cache[i,buying]
        return dfs(0,True)

        