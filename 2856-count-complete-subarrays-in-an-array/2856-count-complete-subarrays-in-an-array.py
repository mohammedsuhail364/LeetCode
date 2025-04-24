from collections import defaultdict
class Solution:
    def countCompleteSubarrays(self, nums) -> int:
        c=len(set(nums))
        l=0
        di=defaultdict(int)
        res=0
        for r in range(len(nums)):
            di[nums[r]]+=1
            while len(di)==c:
                res+=(len(nums)-r)
                di[nums[l]]-=1
                if di[nums[l]]==0:
                    del di[nums[l]]
                l+=1
        return res