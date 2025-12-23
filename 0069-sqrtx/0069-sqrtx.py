class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        l=1
        r=x
        res=0
        while l<=r:
            m=(l+r)//2
            # if m*m<=x: this should be overflow so we can make it like this m<=x//m 
            if m<=x//m:
                res=m
                l=m+1
            elif m>x//m:
                r=m-1
            else:
                l=m+1
        return res