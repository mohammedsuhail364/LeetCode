class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        r=0
        while r<len(nums):
            nums[l]=nums[r] # set the unique value to left
            while r<len(nums) and nums[l]==nums[r]:
                r+=1 # skip the duplicates
            l+=1 # move the left pointer because we find the right (next unique value)
        return l