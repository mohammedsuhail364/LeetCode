class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        res=0
        freq=Counter(nums)
        max_val=max(freq.values())
        for i,j in freq.items():
            if j==max_val:
                res+=max_val
        return res