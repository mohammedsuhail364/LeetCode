class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr=set(nums)
        res=0
        for n in arr:
            length=1
            if (n-1) in arr:
                continue
            while n+length in arr:
                length+=1
            res=max(res,length)
        return res