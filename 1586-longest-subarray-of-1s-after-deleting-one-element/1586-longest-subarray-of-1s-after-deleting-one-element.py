class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        freq=defaultdict(int)
        res=0
        for r in range(len(nums)):
            freq[nums[r]]+=1
            while freq[0]>1:
                freq[nums[l]]-=1
                l+=1
            res=max(res,r-l)
        return res