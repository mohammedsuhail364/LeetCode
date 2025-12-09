class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        h=len(nums)-1
        while l<h:
            if nums[l]+nums[h]==target:
                return [l+1,h+1]
            if nums[l]+nums[h]<target:
                l+=1
            else:
                h-=1
        return [-1,-1]