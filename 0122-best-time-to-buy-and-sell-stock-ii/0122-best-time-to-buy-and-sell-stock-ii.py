class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at any point if the profit increase we can add because for example [7,1,5,8]
        # we can take 5-1 and 8-5 is same as 8-1
        res=0
        for i in range(1,len(prices)):
            c=max(0,prices[i]-prices[i-1]) # to avoid the loss(negatives)
            res+=c
        return res
