class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums=sorted(nums)
        if nums==sorted_nums:
            return 0
        start=0
        end=0
        for i in range(len(nums)):
            if nums[i]!=sorted_nums[i]:
                start=i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i]!=sorted_nums[i]:
                end=i
                break
        return end-start+1
        