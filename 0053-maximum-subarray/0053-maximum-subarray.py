class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=0
        total=-inf
        for i in nums:
            
            if cur<0:
                cur=0
            cur+=i
            total=max(total,cur)
        return total