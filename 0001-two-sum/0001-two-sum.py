class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    res.append(i)
                    res.append(j)
        return res