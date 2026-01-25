class Solution:
    def twoSum(self, nums, target: int):
        l=0
        r=len(nums)-1
        while l<r:
            if nums[l]+nums[r]==target:
                return [l+1,r+1]
            elif nums[l]+nums[r]>target:
                r-=1
            else:
                l+=1
        return [-1,-1]