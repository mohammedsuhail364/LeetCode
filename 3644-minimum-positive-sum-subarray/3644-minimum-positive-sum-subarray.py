class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res=float('inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                k=nums[i:j]
                if l<=len(k)<=r and sum(k)>0:
                    res=min(res,sum(k))

        return res if res!=float('inf') else -1