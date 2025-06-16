class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        res=-1
        max_up_till_now=nums[n-1]
        for i in range(n-2,-1,-1):
            if nums[i]>=max_up_till_now:
                max_up_till_now=nums[i]
            else:
                res=max(res,max_up_till_now-nums[i])
        return res