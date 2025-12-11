class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        res=-inf
        cur_sum=0
        for r in range(len(nums)):
            cur_sum+=nums[r]
            if (r-l+1)>k:
                cur_sum-=nums[l]
                l+=1
            if (r-l+1)==k:
                average=cur_sum/k
                res=max(res,average)
        return res
            