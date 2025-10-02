class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums)
        def helper(nums):
            dp=[0]*(len(nums)+2)
            for i in range(len(nums)-1,-1,-1):
                skip=dp[i+1]
                include=nums[i]+dp[i+2]
                dp[i]=max(skip,include)
            return dp[0]
        case1=helper(nums[:n-1])
        case2=helper(nums[1:])
        return max(case1,case2)

        