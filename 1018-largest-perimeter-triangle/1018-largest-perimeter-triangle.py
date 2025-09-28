class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        i=0
        j=1
        k=2
        res=0
        while k<len(nums):
            if nums[i]+nums[j]>nums[k]:
                res=max(res,nums[i]+nums[j]+nums[k])
            i+=1
            j+=1
            k+=1
        return res