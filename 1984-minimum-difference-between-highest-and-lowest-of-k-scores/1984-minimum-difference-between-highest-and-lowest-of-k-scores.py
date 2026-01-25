class Solution:
    def minimumDifference(self, nums, k: int) -> int:
        if k==1:
            return 0
        nums.sort()
        l=0
        res=inf
        for r in range(k,len(nums)+1):
            res=min(res,nums[r-1]-nums[l])
            l+=1
        return res