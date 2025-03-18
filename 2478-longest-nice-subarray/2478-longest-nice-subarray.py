class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def check(li):
            for i in range(len(li)):
                for j in range(i+1,len(li)):
                    if (li[i]&li[j]) !=0:
                        return False
            return True
        res=1
        l=0
        for r in range(len(nums)):
            k=nums[l:r+1]
            if check(k):
                res=max(res,len(k))
            else:
                l=l+1
        return res