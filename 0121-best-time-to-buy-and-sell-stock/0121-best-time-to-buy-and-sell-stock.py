from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        next_greater=prices[:]
        next_smaller=prices[:]
        for i in range(n-2,-1,-1):
            next_greater[i]=max(prices[i],next_greater[i+1])
        for i in range(1,n):
            next_smaller[i]=min(prices[i],next_smaller[i-1])
        res=0
        for i in range(n):
            res=max(res,next_greater[i]-next_smaller[i])
        return res