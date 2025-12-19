# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        res=0
        l=0
        r=n
        while l<=r:
            m=(l+r)//2
            if isBadVersion(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res
