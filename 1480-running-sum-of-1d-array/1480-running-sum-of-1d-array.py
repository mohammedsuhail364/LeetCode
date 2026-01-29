class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre_sum=[nums[0]]
        for i in range(1,len(nums)):
            pre_sum.append(pre_sum[-1]+nums[i])
        return pre_sum