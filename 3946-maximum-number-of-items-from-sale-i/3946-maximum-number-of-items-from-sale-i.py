class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # this question 
        n=len(items)
        fact=[0]*n
        mini=inf
        for i in range(n):
            mini=min(mini,items[i][1])
            for j in range(n):
                if items[j][0]%items[i][0]==0:
                    fact[i]+=1 # this counts the free's and also self itself like facts[i] contains the j's count and also it self we cannot add after 
        ans=0
        memo=[[-1]*(budget+1) for _ in range(n)]
        def dfs(i,rem):
            if i>=n:
                return rem//mini # we can buy cheapest copies as many as possible
            if memo[i][rem]!=-1:return memo[i][rem]
            # skip the current one
            best=dfs(i+1,rem)
            # include the current one
            price=items[i][1]
            if rem>=price:
                # buy one and get the free
                buy_one=fact[i]+dfs(i+1,rem-price)
                best=max(best,buy_one)
            memo[i][rem] = best
            return memo[i][rem]
        return dfs(0,budget)

            