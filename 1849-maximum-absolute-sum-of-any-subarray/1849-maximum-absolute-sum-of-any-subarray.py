class Solution:
    def maxAbsoluteSum(self, nums) -> int:
        res=0
        min_value=0
        max_value=0
        cur_sum=0
        for n in nums:
            cur_sum+=n
            min_value=min(min_value,cur_sum)
            max_value=max(max_value,cur_sum)
            res=max(res,cur_sum)
            res=max(res,abs(cur_sum-min_value))
            res=max(res,abs(cur_sum-max_value))
        return res