from collections import defaultdict
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l=0
        res=0
        di=defaultdict(int)
        for r in range(len(nums)):
            di[nums[r]]+=1
            while di[nums[r]]>k:
                di[nums[l]]-=1
                l+=1
            res=max(res,(r-l+1))
        return res