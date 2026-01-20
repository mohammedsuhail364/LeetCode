class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        right=-inf
        left=inf
        n=len(nums)
        max_so_far=nums[0]
        for i in range(1,n):
            if nums[i]< max_so_far: # breaks the sorted pattern
                right=i
            else:
                max_so_far=nums[i]
        min_so_far=nums[-1]
        for i in range(n-2,-1,-1):
            if nums[i]>min_so_far:
                left=i
            else:
                min_so_far=nums[i]
        return 0 if right<=left else right-left+1