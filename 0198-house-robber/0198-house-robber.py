class Solution:
    def rob(self, nums: List[int]) -> int:
        cache={}

        def dfs(i):
            if i in cache:
                return cache[i]
            if i>=len(nums):
                return 0
            skip=dfs(i+1)
            include=nums[i]+dfs(i+2)
            cache[i]= max(skip , include)
            return cache[i]
        return dfs(0)