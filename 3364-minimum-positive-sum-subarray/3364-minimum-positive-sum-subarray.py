from cmath import inf


class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        res=inf
        for i in range(len(nums)):
            cur=0
            for j in range(i,len(nums)):
                length = j-i+1
                cur+=nums[j]
                if l<=length<=r and cur>0:
                    res=min(res,cur)
        return res if res!=inf else -1