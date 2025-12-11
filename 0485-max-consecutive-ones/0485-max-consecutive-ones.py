class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        cur=0
        for n in nums:
            if n:
                cur+=1
            else:
                res=max(cur,res)
                cur=0
        res=max(cur,res)
        return res