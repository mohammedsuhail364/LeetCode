class Solution:
    def check(self, nums: List[int]) -> bool:
        check=sorted(nums)
        for i in range(len(nums)):
            nums=nums[1:]+nums[:1]
            if nums==check:
                return True
        return False