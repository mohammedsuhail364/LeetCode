class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        with_out_zero=len(nums)-nums.count(0)
        res=[2]*with_out_zero
        one_count=nums.count(1)
        for i in range(one_count):
            res[i]=1
        final=[0]*nums.count(0)+res
        for i in range(len(nums)):
            nums[i]=final[i]

        