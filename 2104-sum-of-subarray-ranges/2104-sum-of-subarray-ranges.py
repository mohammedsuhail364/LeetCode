class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(n):
            min_val=nums[i]
            max_val=nums[i]
            for j in range(i,n):
                min_val=min(min_val,nums[j])
                max_val=max(max_val,nums[j])
                res+=(max_val-min_val)
        return res