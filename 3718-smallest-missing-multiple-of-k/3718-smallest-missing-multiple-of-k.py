class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums=set(nums)
        x=k
        while True:
            if x not in nums:
                return x
            x+=k
        