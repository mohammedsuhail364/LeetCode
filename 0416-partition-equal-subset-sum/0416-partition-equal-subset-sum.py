class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        
        cache={}
        def dfs(i,cur):
            if (i,cur) in cache:
                return cache[i,cur]
            if i>=len(nums) or cur>total-cur:
                return False
            if cur==total-cur:
                return True
            cache[i,cur] = dfs(i+1,cur) or dfs(i+1,cur+nums[i]) 
            return cache[i,cur]
        return dfs(0,0)