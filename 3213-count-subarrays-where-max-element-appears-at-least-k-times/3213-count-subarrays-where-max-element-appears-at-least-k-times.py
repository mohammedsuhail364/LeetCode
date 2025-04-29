class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val=max(nums)
        di=defaultdict(int)
        l=0
        res=0
        for r in range(len(nums)):
            di[nums[r]]+=1
            while di[max_val]>=k:
                res+=len(nums)-r
                di[nums[l]]-=1
                l+=1
        return res