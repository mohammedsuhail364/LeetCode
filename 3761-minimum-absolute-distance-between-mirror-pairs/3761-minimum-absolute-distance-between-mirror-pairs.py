from math import inf
from typing import List
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen={}
        res=inf
        def reverse(n):
            rev=0
            while n:
                rev=rev*10+ n%10
                n=n//10
            return rev
        for i,n in enumerate(nums):
            if n in seen:
                res=min(res,i-seen[n])
            rev=reverse(n)
            seen[rev]=i
        return res if res!=inf else -1