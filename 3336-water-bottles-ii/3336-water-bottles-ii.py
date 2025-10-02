class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:      
        res=0
        while numBottles>=numExchange:
            res+=(numExchange)
            numBottles=numBottles-numExchange
            numBottles+=1
            numExchange+=1
        if numBottles:
            res+=numBottles
        return res