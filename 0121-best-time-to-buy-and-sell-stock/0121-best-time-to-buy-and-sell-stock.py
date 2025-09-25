class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        profit=0
        for r in range(len(prices)):
            while l<r and prices[l]>prices[r]:
                l+=1
            if prices[l]<prices[r]:
                profit=max(profit,prices[r]-prices[l])
        return profit