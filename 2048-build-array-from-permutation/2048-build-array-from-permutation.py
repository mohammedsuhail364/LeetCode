class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        li=[0]*len(nums)
        for i in range(len(nums)):
            li[i]=nums[nums[i]]
        return li