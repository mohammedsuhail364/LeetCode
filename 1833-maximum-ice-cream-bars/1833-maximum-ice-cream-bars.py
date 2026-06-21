class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res=0
        for c in costs:
            if coins<c:
                break
            coins-=c
            res+=1
        return res