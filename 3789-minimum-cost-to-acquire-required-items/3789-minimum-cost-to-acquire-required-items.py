class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        buyCost1 = cost1*need1
        buyCost2 = cost2*need2
        buyCostBoth = max(need1,need2)*costBoth
        res = min(buyCost1+buyCost2,buyCostBoth)
        # other possibilities
        if need2>need1:
            res = min(res,need1*costBoth + (need2-need1)*cost2) 
        else:
            res = min(res,need1*costBoth) 
            
        if need2<need1:
            res = min(res,need2*costBoth + (need1-need2)*cost1) 
            
        else:
            res = min(res,need2*costBoth) 
            

        return res

        # cost1 = 50,cost2 = 55,costBoth = 72,need1 = 5,need2 = 3
        # =>50*5 + 55*3 = 415
        # =>72*5 = 360
        # =>72*3 + 50*2 = 