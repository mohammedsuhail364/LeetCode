class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res=0
        empty=0
        while numBottles+empty>=numExchange:
            res+=numBottles
            empty+=numBottles
            new_bottle=empty//numExchange
            empty=empty%numExchange
            numBottles=new_bottle
        if numBottles:
            res+=numBottles
        return res