class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=0
        res=-inf
        for n in nums:
            if cur_sum<0:
                cur_sum=0
            cur_sum+=n
            res=max(res,cur_sum)
        return res
