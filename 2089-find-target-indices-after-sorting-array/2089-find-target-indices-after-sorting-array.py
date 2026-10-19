class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res=[]
        for i,v in enumerate(nums):
            if v == target:
                res.append(i)
        return res