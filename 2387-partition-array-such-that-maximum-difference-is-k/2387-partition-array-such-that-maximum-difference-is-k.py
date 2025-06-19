class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        [1,2,3,5,6]
        l=0
        res=0
        r=0
        while r<len(nums):
            while r<len(nums) and l<len(nums) and nums[r]-nums[l]<=k:
                r+=1
            l=r
            res+=1
            
        return res