class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        l=1
        r=x
        while l<=r:
            m=(l+r)//2
            if m==x//m:
                return m
            elif m>x//m:
                r=m-1
            else:
                l=m+1
        return r