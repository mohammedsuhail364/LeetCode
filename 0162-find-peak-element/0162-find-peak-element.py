class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]<nums[m+1]: 
                # increasing state so we can check in the right side 
                # this one only illustrates the which side we can search not the perfect answer
                l=m+1
            else:
                # why we can put only m means we cannot add a condition for equal so it shows less than or equal to 
                r=m
        return l