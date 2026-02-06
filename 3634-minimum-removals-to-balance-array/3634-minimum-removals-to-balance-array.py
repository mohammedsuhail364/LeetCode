class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=inf
        l=0
        cur_sum=0
        for r in range(len(nums)):
            cur_sum+=nums[r]
            while nums[r]>nums[l]*k:
                cur_sum-=nums[l]
                l+=1
            if nums[r]<=nums[l]*k:
                res=min(res,len(nums)-(r-l+1))
        return res if res!=inf else 0