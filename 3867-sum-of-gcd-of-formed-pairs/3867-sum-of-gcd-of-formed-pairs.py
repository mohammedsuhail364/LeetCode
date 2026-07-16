from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        cur_max=0
        gcd_val=[]
        for i in nums:
            cur_max=max(i,cur_max)
            t=gcd(i,cur_max)
            gcd_val.append(t)
        res=0
        gcd_val.sort()
        l=0
        r=len(gcd_val)-1
        while l<r:
            res+=(gcd(gcd_val[l],gcd_val[r]))
            l+=1
            r-=1
        return res