class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        cur_len_inc=1
        cur_len_dec=1
        res=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:cur_len_inc+=1
            else:cur_len_inc=1
            if nums[i]>nums[i+1]:cur_len_dec+=1
            else:cur_len_dec=1

            res=max(res,cur_len_dec,cur_len_inc)
        return res