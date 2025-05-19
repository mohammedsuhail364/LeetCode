class Solution:
    def triangleType(self, nums: List[int]) -> str:
        angles=set(nums)
        if len(angles)==1:
            return "equilateral"
        if len(angles)==2:
            if nums[0]+nums[1]<=nums[2] or nums[0]+nums[2]<=nums[1] or nums[1]+nums[2]<=nums[0]:
                return "none"
            return "isosceles"
        if len(angles)==3:
            if nums[0]+nums[1]<=nums[2] or nums[0]+nums[2]<=nums[1] or nums[1]+nums[2]<=nums[0]:
                return "none"
            return "scalene"