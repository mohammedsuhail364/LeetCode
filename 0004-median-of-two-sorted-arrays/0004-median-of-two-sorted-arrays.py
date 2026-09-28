class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1+nums2
        nums.sort()
        idx = len(nums)//2
        if len(nums)%2:
            return nums[idx]/1
        else:
            return (nums[idx] + nums[idx-1])/2
