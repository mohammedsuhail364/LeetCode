class Solution:
    def countSubarrays(self, nums) -> int:
        res=0
        l=0
        r=3
        while r<len(nums)+1:
            k=nums[l:r]
            q=k[0]+k[-1]
            b=(k[1])/2
            if q==b:
                res+=1
            r+=1
            l+=1
        return res