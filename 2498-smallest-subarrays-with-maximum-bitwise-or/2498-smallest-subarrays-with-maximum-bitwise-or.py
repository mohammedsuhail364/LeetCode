class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # refer statlearn Tech
        n=len(nums)
        res=[1]*n
        for i in range(n):
            cur=nums[i]
            prev=i-1
            while prev>=0 and (nums[prev]|cur)!=nums[prev]:
                res[prev]=i-prev+1
                nums[prev] |= cur
                prev-=1
        return res