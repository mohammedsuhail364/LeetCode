class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res=inf
        l=1
        r=max(piles)
        while l<=r:
            k=(l+r)//2
            hrs=0
            for p in piles:
                hrs+=(ceil(p/k))
            if hrs<=h:
                # have one possible correct answer
                res=min(res,k)
                r=k-1
            else:
                l=k+1
        return res