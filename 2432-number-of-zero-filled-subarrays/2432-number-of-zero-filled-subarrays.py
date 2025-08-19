from collections import defaultdict
from typing import List
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l=0
        freq=defaultdict(int)
        res=0
        for r in range(len(nums)):
            freq[nums[r]]+=1
            while (len(freq)>1 or freq[0]==0) and l<=r:
                freq[nums[l]]-=1
                if freq[nums[l]]==0:
                    del freq[nums[l]]
                l+=1
            res+=(r-l+1)
        return res