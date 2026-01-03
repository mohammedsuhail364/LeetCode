class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        res=0
        while l<=r:
            m=(l+r)//2
            c=0
            for n in nums:
                if n<=m:
                    c+=1
            if c>m:
                res=m # one possible ans
                r=m-1
            else:
                l=m+1
        return res