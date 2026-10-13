class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=[abs(x) for x in nums]
        nums.sort()
        res=0
        l=0
        r=len(nums)-1
        while l<r:
            res+=(nums[r]*nums[r])
            res-=(nums[l]*nums[l])
            l+=1
            r-=1
        if l==r:
            res+=(nums[r]*nums[r])
        return res