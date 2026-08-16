class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c=Counter([s%3 for s in stones])
        c0,c1,c2 = c[0],c[1],c[2]
        if c0%2==0:
            return c1>0 and c2>0
        else:
            return abs(c1-c2)>2
