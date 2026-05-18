from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=inf
        res=0
        for p in prices:
            if p<min_price:
                min_price=p
            if p-min_price>res:
                res=p-min_price
        return res