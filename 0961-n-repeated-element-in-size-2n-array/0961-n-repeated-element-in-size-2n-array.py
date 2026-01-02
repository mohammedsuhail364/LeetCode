class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq=Counter(nums)
        target=len(nums)//2
        for v,c in freq.items():
            if c==target:
                return v
        