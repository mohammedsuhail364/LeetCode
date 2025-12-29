class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        res=0
        while l<r:
            m=(l+r)//2
            if nums[m]<nums[r]:
                # If nums[mid] < nums[right], the right half is sorted, and the minimum is in the left half (possibly mid), so set right = mid.
                r=m
            elif nums[m]>nums[r]:
                # If nums[mid] > nums[right], the minimum is in the right half, so set left = mid + 1.
                l=m+1
            elif nums[r]==nums[m]:
                # duplicates
                r-=1
        return nums[l]