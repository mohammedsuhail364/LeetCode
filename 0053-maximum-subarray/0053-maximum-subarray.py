class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=0
        res=nums[0]
        for n in nums:
            if cur_sum<0:
                cur_sum=0
            cur_sum+=n
            res=max(cur_sum,res)
        return res