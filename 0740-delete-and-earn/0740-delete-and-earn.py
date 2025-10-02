class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        new_nums=[0]*(max(nums)+1)
        print(new_nums)
        di=Counter(nums)
        for i,j in di.items():
            new_nums[i]=(j*i)
        
        # similiar to house robber
        memo={}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i>=len(new_nums):
                return 0
            skip=dfs(i+1)
            include=new_nums[i]+dfs(i+2)
            memo[i] = max(skip,include)
            return memo[i]
        return dfs(0)
