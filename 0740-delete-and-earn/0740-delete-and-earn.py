class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        new_nums=[0]*(max(nums)+1)
        print(new_nums)
        di=Counter(nums)
        for i,j in di.items():
            new_nums[i]=(j*i)
        n=len(new_nums)
        dp=[0]*(n+2)
        # similiar to house robber
        for i in range(n-1,-1,-1):
            skip=dp[i+1]
            include=new_nums[i]+dp[i+2]
            dp[i]=max(skip,include)
        return dp[0]
