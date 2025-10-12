class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        @lru_cache(None)
        def dfs(prev,cur,is_up):
            if cur>=n:
                return 0
            # skip the current one
            skip=dfs(prev,cur+1,is_up)
            # include the current one
            include=0
            if prev==-1 or (nums[prev]<nums[cur] and is_up) or (nums[prev]>nums[cur] and not is_up):
                include=1+dfs(cur,cur+1,not is_up)
            return max(skip,include)
        return max(dfs(-1,0,True),dfs(-1,0,False))