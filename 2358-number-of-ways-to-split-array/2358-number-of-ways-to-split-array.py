class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res=0
        prefix=[0]*len(nums)
        for i,v in enumerate(nums):
            if i==0:
                prefix[i]=v
            else:
                prefix[i]=prefix[i-1]+v  
        for i,v in enumerate(prefix):
            if i==len(prefix)-1:
                continue
            if prefix[i]>=prefix[len(prefix)-1]-prefix[i]:
                res+=1
        return res