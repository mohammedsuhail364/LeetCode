class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=Counter(nums)
        target=int(len(nums)/2)
        for v,f in freq.items():
            if f>target:
                return v
        return -1