class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums)
        memo={}
        def dfs(i,end):
            if (i,end) in memo:
                return memo[i,end]
            if i>=end:
                return 0
            skip=dfs(i+1,end)
            include=nums[i]+dfs(i+2,end)
            memo[i,end]=max(skip,include)
            return memo[i,end]
        case1=dfs(0,n-1)
        case2=dfs(1,n)
        return max(case1,case2)
        