class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)-2):
            if nums[i]==0:
                nums[i]=0 if nums[i] else 1
                nums[i+1]=0 if nums[i+1] else 1
                nums[i+2]=0 if nums[i+2] else 1
                res+=1
        if not nums[-1] or not nums[-2]:
            return -1
        return res