class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        @lru_cache(None)
        def dfs(i,prev,is_up):
            if i>=n:
                return 0
            take=0
            if prev==-1 or (nums[i]>nums[prev] and is_up) or (nums[prev]>nums[i] and not is_up):
                take=1+dfs(i+1,i,not is_up)
            skip=dfs(i+1,prev,is_up)
            res=max(skip,take)
            return res
        return max(dfs(0,-1,True),dfs(0,-1,False))