class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache={}
        def dfs(i,cur):
            if (i,cur) in cache:
                return cache[i,cur]
            if i>=len(nums):
                if cur==target:
                    return 1
                return 0
            add=dfs(i+1,cur+nums[i])
            sub=dfs(i+1,cur-nums[i])
            cache[i,cur] = add+sub
            return cache[i,cur]
        return dfs(0,0)