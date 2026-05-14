class Solution:
    def jump(self, nums: List[int]) -> int:
        cache={}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i>=len(nums)-1:
                return 0
            cache[i]=inf
            for j in range(1,nums[i]+1):
                cache[i]=min(cache[i],1+dfs(i+j))
            return cache[i]
        return dfs(0)