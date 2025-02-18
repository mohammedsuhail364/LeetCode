class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i,total):
            if i==len(nums):
                return total
            x=dfs(i+1,total^nums[i]) # include the nums[i]
            y=dfs(i+1,total) # not include the nums[i]
            return (x+y)
        return dfs(0,0) 