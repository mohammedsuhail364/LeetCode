class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val=max(nums)
        count=0
        l=0
        res=0
        for r in range(len(nums)):
            if nums[r]==max_val:
                count+=1
            while count>=k:
                res+=len(nums)-r
                if nums[l]==max_val:
                    count-=1
                l+=1
        return res