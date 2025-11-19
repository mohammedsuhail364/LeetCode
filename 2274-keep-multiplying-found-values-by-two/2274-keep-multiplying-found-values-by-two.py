class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        res=original
        new_nums=set(nums)
        while res in nums:
            res*=2
        return res