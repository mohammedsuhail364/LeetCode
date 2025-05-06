class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        li=[]
        for i in range(len(nums)):
            li.append(nums[nums[i]])
        return li