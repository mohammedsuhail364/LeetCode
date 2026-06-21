from collections import defaultdict
from typing import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n=max(costs)
        counter=[0]*(n+1)
        for c in costs:
            counter[c]+=1
        res=0
        for cost in range(len(counter)):
            if counter[cost]==0:
                continue
            if cost>coins:
                break
            count=min(counter[cost],coins//cost) # coins//cost -> we can easily find how much we can afford
            coins-=(cost*count)
            res+=count

        return res